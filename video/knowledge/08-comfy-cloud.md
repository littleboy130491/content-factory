# 08 — Comfy Cloud (MCP)

## Tool utama
| Tool | Untuk |
|---|---|
| `partner_generate` | Gambar dari model partner (Nano Banana, Seedream). Edit gambar: `medias` dengan `name` hasil upload |
| `run_template` | Template seperti `api_kling_v3_video`, `video_minimax_h3_r2v`, lewat `input_overrides` |
| `submit_workflow` | Graph format API penuh (mis. H3 dengan >2 referensi dari `scripts/h3_build.py`) |
| `submit_batch` | Banyak job, satu konfirmasi biaya. `medias` hanya menerima `name`/`value`, **bukan** `prompt_id` |
| `upload_file` | URL PUT sekali pakai. Jalankan sendiri `curl -X PUT -H 'Content-Type: image/png' --upload-file <file> <url>`. Nama yang kembali = hash isi file |
| `wait_for_job` / `get_output` / `get_batch_output` | Menunggu dan mengambil hasil |

## Spend gate
Panggilan berbayar pertama mengembalikan permintaan konfirmasi. Panggil ulang dengan `confirm: true` **hanya** setelah user setuju secara eksplisit. Satu konfirmasi `submit_batch` berlaku untuk seluruh batch.

## Quirk yang sudah ditemui
- `wait_for_batch` kadang salah status ("pending" padahal selesai) dan bisa timeout. Pakai `wait_for_job` per job atau `get_batch_output`.
- `wait_for_job` dengan `max_wait_seconds` 300 bisa kena batas waktu tool sekitar 230 dtk. Ambil hasilnya dengan `get_batch_output`.
- Sesi bisa kedaluwarsa ("session is invalid or expired"). Job yang sudah dikirim tetap jalan; minta user login ulang, lalu ambil hasilnya.
- Kredit habis → "out of credits", tidak ada yang ditagih. Jangan retry sebelum diisi.
- Hasil multi-referensi Nano Banana Pro jatuh ke direct dispatch dan tidak tersimpan di library.
- URL unduhan `/api/s/…` kedaluwarsa sekitar 5 menit; URL storage bertanda tangan sekitar 6 jam.

## Template Kling: `api_kling_v3_video`
- Node `1` LoadImage berisi `image`.
- Node `3` KlingVideoNode berisi:
  - `multi_shot: "disabled"`
  - `multi_shot.prompt`
  - `multi_shot.negative_prompt`
  - `multi_shot.duration` (int)
  - `generate_audio`
  - `model: "kling-v3"`
  - `model.resolution: "1080p"`
  - `model.aspect_ratio: "9:16"`
  - `seed`

  Tanpa input frame akhir. Bentuk item batch: `scripts/kling_batch.py`.

## Template H3: `video_minimax_h3_r2v`
- Node pentingnya:

  | Node | Isi |
  |---|---|
  | 115 | ResolutionSelector (`9:16 (Portrait Widescreen)`, 0.6 MP) |
  | 129 | `noise_seed` |
  | 132 | durasi (float) |
  | 137 | ref 1 |
  | 139 | ref 2 |
  | 138 | prompt |
  | 146 | turbo on/off |

- Untuk lebih dari 2 referensi pakai `scripts/h3_build.py` + `submit_workflow`.
- Model yang dipakai:
  - UNET `minimax_h3_ref2va_pruned_int8_convrot`
  - CLIP `qwen3vl_32b_minimax_h3_nvfp4_awq` (type `minimax`)
  - LoRA `minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16` (4 step, sampler `res_multistep`)
- Workflow aslinya ada di `workflows/minimax_h3_r2v_turbo.json` (format save, bisa dibuka di ComfyUI).

## Seedream
`model: "byteplus/images-generations"`, `params: {"model": "seedream 5.0 flash"}`, `medias: [{"role": "reference_image", "name": "<upload>"}]`. Di prompt sebut "Image 1 is …".
