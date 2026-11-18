# 03 — Model & provider (status Nov 2026)

## Gambar
| Model | Pakai untuk | Kekuatan | Quirk / kelemahan |
|---|---|---|---|
| **Nano Banana Pro** (Google Gemini) | Referensi & keyframe realistis | Multi-referensi kuat, wajah konsisten, 9:16 native | ~$0.17/gambar; lewat Comfy, hasil multi-ref **tidak tersimpan di library** (harus diunduh lalu di-upload ulang) |
| **Seedream 5.0 Flash** (ByteDance/BytePlus) | Referensi & keyframe anime/ilustrasi | Murah, gaya kuat, konsistensi dari ref image bagus | **Selalu 1024×1024**: `size`/`aspect_ratio` diabaikan. Crop ke 9:16 (`scripts/crop_to_vertical.py`) atau pakai model lain untuk komposisi vertikal |
| Seedream 5.0 Pro / 5.5 | Alternatif keyframe | Belum diuji untuk 9:16 | — |
| GPT Image, Qwen Image | Alternatif | Belum diuji di pipeline ini | — |

Nama `params.model` Seedream yang valid: `seedream 5.5`, `seedream 5.0 pro`, `seedream 5.0 flash`, `seedream 5.0 lite`, `seedream-4-5-251128`, `seedream-4-0-250828`.

## Video
| Model | Mode | Hasil | Catatan |
|---|---|---|---|
| **Kling 3.0** | image-to-video | 1080p, 3–10 dtk, audio opsional | Paling stabil untuk wajah. Gaya keyframe (termasuk anime cel) dipertahankan. Gerak terlalu halus untuk anime (turunkan ke 12 fps saat edit). Patuh pada aksi sederhana, tapi **mengarang** kalau diminta interaksi tangan dengan benda kecil |
| **MiniMax H3 ref2v turbo** (open-weights, LoRA 4-step) | reference-to-video, multi-shot | 608×1056, 24fps, audio stereo, 5–15 dtk | Sampai 9 referensi per generate. Format "Shot N \| a-bs: … Hard cut." Butuh GPU (ComfyUI). ~2–3 menit per generate |
| **Wan 2.2** | i2v/t2v open-weights | — | **Jangan dipakai:** lambat, mahal di GPU cloud, mengarang teks/label |
| Seedance 2.0 r2v | reference-to-video | Belum diuji | Kandidat pengganti H3 yang bisa dipanggil sebagai API |

## Aturan memilih
1. Wajah tokoh utama dalam close-up → keyframe + Kling.
2. Banyak shot suasana/figuran dengan gaya sama → H3 multi-shot.
3. Butuh tanpa GPU sendiri / API langsung → Nano Banana atau Seedream + Kling.
4. Teks di layar → mockup HTML, bukan model.
