# 09 — Pasca-produksi

## Rough cut
`scripts/roughcut.py edit.json --dir <folder klip>`. Edit list per proyek disimpan di `project/<nama>/`.
- Normalisasi semua klip ke ukuran target (default 1080×1920) dan 24 fps.
- **Grain seragam** (`noise=alls=6:allf=t`) membuat klip dari model berbeda terasa satu film.
- **Rasa anime "on twos":** `anime_twos: true`, yaitu `fps=12` lalu `fps=24`.
- **Audio H3:** `keep_audio: true`; klip tanpa audio diberi audio hening supaya concat tidak rusak.

## Upscale
- Output H3 608×1056 → 1080×1920. Lanczos di ffmpeg sudah cukup untuk draf. Untuk final, pertimbangkan upscaler model (ESRGAN/anime upscaler di ComfyUI) dan cek wajah setelahnya.

## Teks & UI
- Layar HP/website/chat dibuat sebagai mockup HTML, lalu direkam dengan headless Chrome. Teksnya dijamin sesuai naskah.
- Kartu teks dan judul ditambahkan saat edit, tidak digenerate.

## Sound
- Ambience per ruang + foley kecil (bel pintu, plastik, kipas, jam dinding). Tanpa musik kecuali diminta.
- Kling tanpa audio → sound dari library atau generate audio terpisah.

## Export
- Vertikal 1080×1920, H.264, `-preset veryfast` untuk draf (lebih lambat hanya kalau diminta kualitas terbaik), `-crf 18–20`, `yuv420p`.
- Kirim preview ke user secepat mungkin, lalu iterasi.
