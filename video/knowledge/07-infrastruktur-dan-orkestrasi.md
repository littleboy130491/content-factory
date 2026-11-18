# 07 — Infrastruktur & orkestrasi

## Opsi
| Opsi | Cocok untuk | Catatan |
|---|---|---|
| **Comfy Cloud** (lewat MCP) | Eksperimen, campuran model partner + open-weights | Paling praktis. Risiko: sesi kedaluwarsa, kredit habis |
| **RunPod / Vast + ComfyUI headless** | Volume tinggi model open-weights (H3, Wan, upscaler, LoRA) | Lebih murah per jam, tapi setup dan unduh model sendiri. Kirim graph lewat endpoint `/prompt` |
| **RunComfy, Higgsfield GPU** | Alternatif GPU terkelola | Bandingkan harga per jam dengan Comfy Cloud |
| **API langsung** (Gemini, BytePlus, Kling, MiniMax) | Produksi rutin dengan model partner | Tanpa perantara, kontrol penuh (seed, webhook, start+end frame Kling). Tagihan terpisah per vendor |

## Rekomendasi: hibrida
- Model partner (Nano Banana, Seedream, Kling) → **API langsung**.
- Model open-weights (H3 turbo, upscaler, LoRA) → **ComfyUI sebagai GPU worker**.
- Trim, grain, concat, upscale sederhana → **ffmpeg lokal**.

## Yang harus disiapkan kalau lepas dari Comfy
- Penyimpanan aset di S3/R2 (referensi, keyframe, klip) dengan URL publik sementara untuk provider.
- Antrean job: polling/webhook, retry, batas rate per provider.
- API key per provider di `.env` atau secret manager. **Jangan pernah** ditulis di repo, di-print, atau di log.
- Pencatatan biaya per job dan per proyek.

## Kerangka orkestrator (rencana)
```
projects/<nama>/shotlist.json
  → refs     : generate + approve referensi
  → keyframes: per shot, provider gambar
  → videos   : per shot (Kling) atau per adegan (H3)
  → qa       : contact sheet + tanda untuk review manusia
  → edit     : roughcut.py
```
Setiap langkah idempoten (skip kalau file sudah ada) dan menulis `manifest.json` per proyek: prompt, seed, provider, biaya, status QA, path file.
