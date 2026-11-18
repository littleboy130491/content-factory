# 01 — Prinsip & gaya

## Prinsip kreatif
- **Film pendek, bukan iklan.** Cerita jalan lewat perilaku dan kontras sebelum/sesudah. Tidak ada yang menjelaskan pesan.
- **Sinematografi diutamakan:** cahaya, udara (debu di sinar, uap, kabut kaca), arah sinar matahari sesuai jam, lensa yang tenang.
- **Natural, tidak terlihat buatan AI.** Detail aus dan tidak sempurna (cat terkelupas, kabel, ember, kalender) membuat lokasi terasa nyata. Lokasi yang terlalu rapi terlihat seperti render.
- **Konsistensi wajah dan ekspresi natural itu wajib.** Ekspresi kecil (senyum tipis bibir tertutup, kedip pelan, napas) lebih dipercaya daripada ekspresi besar.
- **Subtle lebih baik daripada berlebihan.** Detail cerita (misalnya barang salah taruh) diletakkan untuk penonton yang jeli, tidak ditunjuk-tunjuk.

## Prinsip produksi
- **Kunci dulu, baru gerak.** Urutannya: karakter → lokasi → keyframe → video. Setiap tahap diapprove sebelum lanjut, karena makin ke belakang makin mahal untuk diulang.
- **Berikan 2 opsi** untuk aset kunci (wajah, lokasi), lalu minta user memilih.
- **Satu shot, satu aksi sederhana.** Lihat [05-qa-dan-halusinasi.md](05-qa-dan-halusinasi.md).
- **Halusinasi objek adalah kesalahan paling fatal.** Klip seperti itu dibuang atau diulang, tidak boleh disembunyikan.
- **Jangan keluarkan kredit tanpa "ya" eksplisit dari user,** dan sebutkan perkiraan biaya lebih dulu.
- **Draf cepat, lalu iterasi.** Kirim hasil antara (keyframe, tes 3 klip) sedini mungkin supaya arah bisa dikoreksi.

## Tokoh & representasi
- Untuk tokoh Indonesia, tulis etnis, umur, warna kulit, rambut, dan pakaian di **setiap** prompt referensi dan keyframe.
- Figuran (pelanggan, keluarga) paling aman **selalu dari belakang**. Ini menghemat konsistensi wajah dan mengurangi risiko.
- Tanpa dialog kecuali diminta. Tulis "mouths stay closed" supaya model tidak membuat gerak bibir.

## Gaya yang sudah teruji
| Gaya | Kunci prompt | Catatan |
|---|---|---|
| Realistis dokumenter | `Natural real-time motion, documentary realism, 35mm film grain.` | Kling 3.0 + keyframe Nano Banana Pro |
| Anime TV 90-an | lihat `templates/prompts/style-anime90.txt` | Seedream untuk gambar; H3 atau Kling untuk gerak |
