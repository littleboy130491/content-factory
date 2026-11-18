# 05 — QA & halusinasi

## Istilah
**Halusinasi objek / kesalahan logika-kontinuitas:** model memunculkan, menghilangkan, atau mengubah benda/kejadian tanpa sebab dalam adegan. Ini setara dengan *continuity error* dalam film. **Ini kesalahan paling fatal**, karena penonton langsung sadar videonya buatan AI.

Contoh nyata: prompt "wipes his hand once on his apron" menghasilkan tangan masuk ke balik apron dan tiba-tiba ada kantong/kain.

## Pemicu umum
1. Interaksi tangan dengan benda kecil atau kain: mengelap, memasukkan ke saku, membuka bungkus, memutar kantong plastik.
2. Beberapa aksi berurutan dalam satu shot.
3. Gerak kepala/badan untuk tokoh yang harus membelakangi kamera.
4. Durasi panjang tanpa aksi yang jelas: model mengisi kekosongan dengan karangan.
5. Teks dan angka di benda.

## Pencegahan
1. Satu shot, satu aksi sederhana.
2. Kunci frame awal (keyframe). Frame akhir juga kalau provider mendukung (Kling API langsung mendukung; template Comfy `api_kling_v3_video` tidak).
3. Tulis yang harus diam ("stays exactly as it is").
4. Negative prompt standar (`templates/prompts/negative.txt`).
5. Generate 2 versi untuk shot penting, pilih yang bersih.
6. Potong klip sebelum kesalahan muncul. Banyak klip tetap bisa dipakai 2–3 detik pertamanya.

## Checklist per klip
Buat contact sheet (`scripts/contact_sheet.py --frames 8`), lalu periksa:

**Fatal: buang/ulang**
- [ ] Benda muncul, hilang, atau berubah tanpa sebab
- [ ] Pelanggaran fisika: tangan menembus benda, masuk ke baju, benda melayang
- [ ] Identitas berubah: wajah berbeda dari referensi
- [ ] Wajah yang harus tersembunyi jadi terlihat
- [ ] Tubuh cacat: jari bertambah, anggota badan meleleh

**Mayor: perbaiki atau trim**
- [ ] Mulut bergerak / seperti bicara
- [ ] Ekspresi berlebihan (senyum lebar, gigi terlihat bila dilarang)
- [ ] Teks atau label jadi acak
- [ ] Gaya bergeser (anime jadi 3D/glossy; realistis jadi plastik)
- [ ] Cahaya tidak sesuai waktu adegan

**Minor: catat**
- [ ] Gerak terlalu halus untuk gaya anime
- [ ] Waktu hard cut multi-shot meleset lebih dari 1 dtk
- [ ] Flicker kecil di latar

## Melapor ke user
Laporkan jujur per shot: apa yang berhasil, apa yang gagal, dan rencana perbaikannya. Jangan kirim klip yang gagal tanpa menyebut masalahnya.
