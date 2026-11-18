# Invisible Mistakes

Film pendek vertikal untuk sebuah toko roti kecil: kesalahan-kesalahan kecil yang tidak terlihat (roti salah taruh, cake rusak, kasir kosong) diam-diam membuat pelanggan pergi.

- **Klien:** toko roti (proyek imajiner.id)
- **Mulai:** Nov 2026
- **Format:** 9:16, ±100 dtk, tanpa dialog
- **Bible (dokumen kolaboratif):** https://claude.ai/artifact/QR1xdumrHWTer6KoMh2dDd. Isinya arah, cahaya, karakter, shot list, aturan produksi.

## Status (18 Nov 2026)
| Versi | Jalur | Status |
|---|---|---|
| Realistis | Nano Banana Pro keyframe → Kling 3.0 | 22 shot selesai, rough cut v1 jadi. Belum: bagian HP, kartu teks, VO/sound |
| Anime 90-an (H3) | Seedream ref → MiniMax H3 multi-shot | 9 adegan sudah digenerate di Comfy Cloud, **belum diunduh dan direview** |
| Anime 90-an (tanpa r2v) | Seedream keyframe → Kling 3.0 | Tes 3 shot: malam berhasil; pagi halusinasi; sore wajah terlihat. Ulang pagi/sore dengan prompt v2, **tertunda karena kredit Comfy habis** |

## Isi folder
| Path | Isi |
|---|---|
| [cerita-dan-karakter.md](cerita-dan-karakter.md) | Tokoh, lokasi, alur adegan, shot list ringkas |
| [log-keputusan.md](log-keputusan.md) | Revisi dari user dan keputusan, berurutan |
| `prompts/anime_h3_scenes.json` | 9 adegan H3 (gaya, referensi, seed, durasi, prompt) |
| `prompts/realistic_kling_shots.json` | Prompt Kling shot 02–21 versi realistis |
| `prompts/realistic_edit.json` | Edit list rough cut v1 realistis |
| `prompts/anime_keyframe_kling_test.json` | Tes anime tanpa r2v, termasuk prompt v2 yang belum dijalankan |
| `refs/realistic/`, `refs/anime/` | Referensi yang diapprove (JPG terkompres) |
| `samples/` | Contact sheet hasil tes |

Nama `image` di JSON adalah **hash upload Comfy Cloud** di akun imajiner. Di akun lain, upload ulang file dari `refs/`, lalu ganti namanya.

## Cara mengulang
```bash
cd video
# H3 (anime): bangun graph untuk adegan tertentu → kirim lewat submit_batch (tool submit_workflow)
python3 scripts/h3_build.py projects/invisible-mistakes/prompts/anime_h3_scenes.json -o /tmp/h3.json --only A2_keluarga A9_malam
# Kling (realistis): item batch
python3 scripts/kling_batch.py projects/invisible-mistakes/prompts/realistic_kling_shots.json -o /tmp/kling.json
# Rough cut realistis (klip vid01..vid22.mp4 di folder vid/)
python3 scripts/roughcut.py projects/invisible-mistakes/prompts/realistic_edit.json --dir vid
```

## Berikutnya
1. Ambil dan review 9 adegan H3, lalu bandingkan dengan jalur Kling.
2. Ulang shot pagi/sore jalur Kling (seed 411/412) setelah kredit diisi.
3. Pilih jalur anime final, lalu buat rough cut anime (upscale 1080×1920, `anime_twos`).
4. Bagian HP (mockup HTML), kartu teks, sound.
