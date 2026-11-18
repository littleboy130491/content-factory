# 02 — Pipeline produksi

```
brief/storyboard → bible → referensi (karakter, lokasi, varian cahaya) → keyframe per shot
→ video → QA → trim & rough cut → teks/UI → sound → export
```

## Rekomendasi: bertahap, dari murah ke mahal
Pelajaran dari proyek pertama (lihat `diary/2026-11-18-invisible-mistakes.md`): cerita dan gaya berubah **setelah** produksi resolusi tinggi selesai, jadi biayanya terbuang. Mulai sekarang setiap proyek melewati gerbang ini:

| Fase | Output | Gerbang yang dikunci |
|---|---|---|
| 0. Brief | Bible v0, referensi visual dari user berupa **gambar** | Arah |
| 1. Sketsa storyboard | 1 frame kasar per shot, resolusi rendah / model termurah | Cerita & komposisi |
| 2. Animatic | Sketsa + durasi per shot + audio kasar (ffmpeg) | **Ritme & durasi** (variasikan!) |
| 3. Tes gaya | 1 shot kunci dalam 2–3 gaya, termasuk 1 klip gerak | **Gaya** |
| 4. Referensi | Karakter & lokasi final, 2 opsi | Wajah & lokasi |
| 5. Motion draft | Semua shot bergerak, resolusi rendah (mis. H3 turbo 0.6 MP) | Aksi bebas halusinasi |
| 6. Final | Hanya shot yang lolos: keyframe hi-res, lalu video 1080p | QA lolos |
| 7. Edit | Rough cut, teks/UI, sound | Approve user |

Proyek kecil boleh menggabungkan fase (mis. 1+2, atau 4+5), tapi **jangan pernah melompat ke fase 6 sebelum cerita, ritme, dan gaya dikunci**.

## 1. Bible
Tulis ulang storyboard menjadi bible (template: `templates/bible.md`). Isinya arah, cahaya & udara, kamera & look, karakter, lokasi, shot list, dan rencana aset. Simpan sebagai dokumen yang bisa dikomentari user. Setiap revisi user langsung masuk ke bible.

## 2. Referensi
- **Karakter:** potret setengah badan dengan pakaian final, cahaya netral. Buat 2 opsi.
- **Lokasi:** satu interior master, lalu varian cahaya (pagi, siang, sore, malam) yang **dibuat dari master** supaya tata letaknya sama.
- **Figuran:** cukup dari belakang: pakaian, rambut, aksesori.

## 3. Keyframe (gambar per shot)
Model gambar multi-referensi menerima referensi karakter dan lokasi. Satu keyframe per shot, lalu diapprove. Shot yang direvisi diberi versi (`kf09v2`).

## 4. Video — tiga jalur yang teruji

| Jalur | Alur | Kuat | Lemah |
|---|---|---|---|
| **A. Keyframe → i2v** | keyframe → Kling 3.0 | 1080p, gaya terkunci, kontrol per shot, bisa lewat API langsung | 1 shot per generate, tanpa audio (opsional), lebih mahal |
| **B. Reference-to-video multi-shot** | referensi → MiniMax H3 (2–4 shot dengan hard cut per generate) | sangat efisien, audio ikut, tanpa tahap keyframe | 608×1056 (perlu upscale), timing cut meleset ±1 dtk, butuh GPU |
| **C. Hibrida** | B untuk shot suasana/insert, A untuk shot wajah penting | seimbang | dua pipeline untuk dirawat |

Pilihannya:
- Kualitas dan kontrol per shot penting → **A**.
- Volume, biaya, dan kecepatan penting → **B**.

## 5. QA
Setiap klip dicek dengan contact sheet (`scripts/contact_sheet.py`) dan checklist di [05](05-qa-dan-halusinasi.md). Klip yang gagal diulang dengan prompt lebih sederhana, bukan sekadar seed lain.

## 6. Edit
- `scripts/roughcut.py` memakai edit list JSON: normalisasi ukuran/fps, grain seragam, trim, concat.
- Durasi per shot sengaja bervariasi (2–6 dtk). Ritme datang dari edit, bukan dari panjang generate.

## 7. Teks, UI, sound
- Layar dengan teks pasti (chat, website, HP) dibuat sebagai mockup HTML lalu direkam/screenshot. Jangan digenerate.
- Kartu teks ditambahkan lokal.
- Sound: ambience per ruang + foley kecil. H3 sudah membawa ambience; Kling (tanpa audio) perlu sound terpisah.
