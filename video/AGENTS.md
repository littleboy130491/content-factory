# AGENTS.md — Video (produksi film pendek AI)

Instruksi untuk AI agent mana pun (Claude, Codex, Gemini, dll.) yang bekerja di folder `video/`. Baca sampai habis sebelum memulai. Aturan bahasa dan selera penulis di `CLAUDE.md` root repo tetap berlaku.

## 1. Apa folder ini
Basis pengetahuan dan alat untuk membuat **film pendek dengan AI** (gambar → video → edit) bagi imajiner.id dan kliennya. Isinya dipisah menjadi:

| Folder | Isi | Kapan dibaca |
|---|---|---|
| `knowledge/` | **Pengetahuan global:** prinsip, pipeline, model, prompting, QA, biaya, infrastruktur, Comfy, pasca-produksi | **Selalu**, sesuai kebutuhan tugas (mulai dari `knowledge/README.md`) |
| `diary/` | Catatan eksperimen & refleksi per proyek: apa yang gagal, apa yang berhasil, trade-off | Baca `diary/README.md` (bagian "Pelajaran terpenting") di awal setiap proyek baru |
| `templates/` | Template bible, README proyek, entri diary, dan prompt (gaya, keyframe, video, multi-shot, negative) | Saat memulai proyek atau menulis prompt |
| `scripts/` | Skrip generik: `h3_build.py`, `kling_batch.py`, `roughcut.py`, `contact_sheet.py`, `crop_to_vertical.py` | Saat membangun batch, QA, atau rough cut |
| `workflows/` | Workflow ComfyUI (format save) | Saat butuh graph aslinya |
| `projects/` | **Pengetahuan khusus proyek:** cerita, karakter, log keputusan, data prompt, referensi | **Hanya kalau user memintanya** (lihat §2) |

## 2. Aturan folder `projects/` — penting
- **Jangan membuka, me-list, atau mencari di `projects/`** kecuali:
  1. user menyuruh memakai proyek tertentu sebagai referensi ("pakai Invisible Mistakes sebagai acuan"), atau
  2. user meminta melanjutkan proyek itu sendiri.
- Alasannya: isi proyek (karakter, cerita, prompt adegan) akan mencemari proyek baru dan memenuhi konteks. Pelajaran yang berlaku umum **sudah disuling** ke `knowledge/` dan `diary/`.
- Kalau diizinkan, baca hanya proyek yang disebut, mulai dari `README.md`-nya.
- Proyek baru dibuat di `projects/<nama-kebab-case>/` dari `templates/project-readme.md`.

## 3. Alur kerja proyek baru (ringkas)
Detail di `knowledge/02-pipeline.md`. **Bertahap, dari murah ke mahal, dengan gerbang persetujuan user:**
1. **Brief → bible v0.** Minta referensi visual sebagai gambar, bukan link video.
2. **Sketsa storyboard** murah dan resolusi rendah, sampai cerita dan komposisi dikunci.
3. **Animatic:** sketsa dengan durasi per shot. **Ritme dan variasi durasi** dikunci di sini.
4. **Tes gaya:** 1 shot kunci dalam 2–3 gaya, sampai gaya dikunci.
5. **Referensi karakter dan lokasi:** 2 opsi per aset, user memilih.
6. **Motion draft resolusi rendah** untuk semua shot, sampai aksi bebas halusinasi.
7. **Final resolusi tinggi** hanya untuk shot yang lolos.
8. **Edit:** rough cut, teks/UI (mockup HTML), sound.

Proyek kecil boleh menggabungkan fase, tapi **jangan melompat ke resolusi tinggi sebelum cerita, ritme, dan gaya dikunci**.

## 4. Aturan produksi (wajib)
1. **Satu shot, satu aksi sederhana.** Tidak ada interaksi tangan dengan benda kecil (mengelap, saku, bungkus) dan tidak ada aksi berlapis. Ini pemicu utama halusinasi.
2. **Halusinasi objek** (benda muncul, hilang, atau berubah tanpa sebab) **adalah kesalahan paling fatal.** Klipnya dibuang atau diulang dengan prompt yang lebih sederhana, tidak disembunyikan.
3. **Setiap klip di-QA** dengan `scripts/contact_sheet.py` dan checklist di `knowledge/05-qa-dan-halusinasi.md` sebelum dipakai atau dikirim.
4. **Negative prompt standar** dari `templates/prompts/negative.txt` selalu dipakai.
5. **Figuran selalu dari belakang.** Untuk tokoh yang membelakangi kamera, jangan menulis gerak kepala.
6. **Tanpa dialog** kecuali diminta. Tulis "mouths stay closed".
7. **Teks di layar (chat, website, HP, kartu)** dibuat sebagai mockup HTML atau ditambahkan saat edit, tidak digenerate.
8. **Cek ukuran dan format output** setiap model baru dari hasil pertama, sebelum merencanakan batch.
9. **Selesaikan evaluasi satu jalur** (unduh, contact sheet, laporan) sebelum membuka jalur baru.
10. **Shot penting digenerate 2 versi,** lalu pilih yang paling bersih.

## 5. Biaya & izin
- **Jangan pernah mengeluarkan kredit atau biaya tanpa "ya" eksplisit dari user.** Sebutkan perkiraan dalam USD dan Rupiah (±Rp17.700/USD, cek ulang kursnya) dan apa saja yang akan dijalankan.
- Jalankan **tes 3 klip** dulu sebelum batch penuh.
- Catat biaya berjalan per proyek dan cek saldo sebelum batch besar.
- API key ada di `.env` root (mis. `MINIMAX_API_KEY`). **Jangan pernah** membaca, mencetak, atau menulis key ke file atau log. Muat lewat `set -a; . ./.env; set +a` dan pakai nama variabelnya saja.

## 6. Pilihan model (ringkas, status Nov 2026)
Detail dan quirk di `knowledge/03-model-dan-provider.md`.
- **Keyframe realistis:** Nano Banana Pro (multi-ref, 9:16 native).
- **Keyframe anime/ilustrasi:** Seedream 5.0 Flash. **Output selalu 1024×1024**, jadi pakai `scripts/crop_to_vertical.py`.
- **Video dari keyframe:** Kling 3.0, 1080p.
- **Multi-shot murah + audio:** MiniMax H3 ref2v turbo (608×1056, butuh GPU/ComfyUI).
- **Hindari:** Wan 2.2.

## 7. Bahasa & komunikasi
- Bahasa Indonesia untuk dokumen dan balasan ke user. Istilah produksi (shot, close-up, keyframe, prompt) tetap bahasa Inggris. Prompt ke model ditulis dalam bahasa Inggris.
- Kirim hasil antara secepatnya (keyframe, tes klip, contact sheet), dan laporkan jujur per shot apa yang berhasil dan apa yang gagal.
- Kalau user bertanya "apa baiknya…?", beri satu rekomendasi dengan trade-off-nya.

## 8. Merawat pengetahuan
- Keputusan dan revisi user ditulis di `projects/<nama>/log-keputusan.md`.
- Di akhir sesi atau proyek, tulis entri `diary/` (template: `templates/diary-entry.md`): yang dilakukan, gagal, berhasil, trade-off, refleksi.
- Temuan yang berlaku umum dipindahkan ke `knowledge/` dengan tanggal. Angka yang usang dikoreksi, jangan dibiarkan.
- Jangan menyalin isi proyek mentah ke `knowledge/`. Sulingan saja.

## 9. Struktur file proyek
```
projects/<nama>/
  README.md              status, isi folder, cara mengulang
  cerita-dan-karakter.md tokoh, lokasi, alur adegan
  log-keputusan.md       keputusan & revisi user, berurutan
  prompts/*.json         data untuk scripts/ (adegan, shot, edit list)
  refs/                  referensi yang diapprove (JPG terkompres, maks ~1024 px)
  samples/               contact sheet QA
```
Video mentah (`*.mp4`) **tidak** di-commit. Simpan di storage terpisah dan catat lokasinya di README proyek.
