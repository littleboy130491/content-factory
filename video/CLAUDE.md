# CLAUDE.md — Video

Semua aturan di AGENTS.md berlaku. Bagian di bawahnya khusus untuk Claude.

@AGENTS.md

## Khusus Claude

### Urutan membaca di awal tugas video
1. File ini dan `AGENTS.md` (sudah termuat).
2. `diary/README.md`, bagian "Pelajaran terpenting".
3. File `knowledge/` yang relevan dengan langkah yang sedang dikerjakan. Tidak perlu semuanya; pilih dari tabel di `knowledge/README.md`.
4. **`projects/` tidak dibuka**, kecuali user menyebut proyeknya atau meminta memakainya sebagai referensi (AGENTS.md §2).

### Comfy Cloud MCP
- Detail tool, quirk, dan node template ada di `knowledge/08-comfy-cloud.md`.
- **Spend gate:** panggilan pertama tanpa `confirm`, lalu tanyakan biayanya ke user, lalu panggil ulang dengan `confirm: true` hanya setelah user bilang "ya", "lanjut", "go", atau sejenisnya untuk pengeluaran itu.
- Generate lebih dari 1 item → satu `submit_batch`, bukan banyak panggilan terpisah.
- Upload: `upload_file` memberi URL PUT, lalu jalankan sendiri `curl -X PUT` di shell. Nama file yang kembali dipakai di LoadImage atau `medias[].name`.
- Menunggu: `wait_for_job` per job (bisa timeout sekitar 230 dtk, tinggal dipanggil lagi) atau `get_batch_output`. Jangan bergantung pada `wait_for_batch`.
- Error "session invalid/expired" → minta user menyambungkan ulang konektor Comfy. Job yang sudah terkirim tetap jalan.
- Error "out of credits" → berhenti, beri tahu user, jangan retry.

### Alat kerja
- Pakai daftar tugas (TaskCreate/TaskUpdate) untuk pekerjaan multi-langkah. Langkah terakhirnya selalu QA hasil.
- Lihat setiap gambar dan contact sheet dengan Read sebelum mengirim atau memakainya.
- Kirim hasil (video, contact sheet, keyframe) ke user dengan SendUserFile, dengan caption satu baris.
- Bible proyek dibuat sebagai dokumen kolaboratif (Claude Docs) supaya user bisa berkomentar. Simpan link-nya di `projects/<nama>/README.md`.
- Encode draf dengan `-preset veryfast`.

### Gaya kerja dengan user ini
- User memutuskan cepat dan menyukai satu rekomendasi yang jelas. Draf pertama untuk didorong-dorong, bukan untuk sempurna.
- Kritik user seperti "terlalu obvious", "lebih real", "lebih ramah" adalah arah, bukan instruksi literal. Terjemahkan ke perubahan konkret, lalu berikan 2 opsi.
- Akui kesalahan sendiri dengan jelas (mis. prompt yang memicu halusinasi), lalu langsung beri perbaikan.

### Di akhir sesi
- Perbarui `projects/<nama>/README.md` (status) dan `log-keputusan.md`.
- Tulis atau perbarui entri `diary/`.
- Pindahkan pelajaran umum ke `knowledge/`.
