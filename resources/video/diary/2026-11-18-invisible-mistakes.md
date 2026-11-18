# 2026-11-18 — Invisible Mistakes: realistis → anime 90-an

> Ditulis oleh agent yang mengerjakan proyek ini (Claude), sebagai bekal untuk agent atau orang berikutnya. Ditulis jujur, termasuk kesalahan sendiri.

## Konteks
User (pemilik imajiner.id) memberikan storyboard PDF untuk film pendek vertikal ±100 detik tentang toko roti. Permintaannya: terasa seperti film pendek dengan sinematografi bagus, bukan iklan; tidak terlihat buatan AI; cahaya dan udara diperhatikan; wajah konsisten dan ekspresi natural.

## Kronologi singkat
| Fase | Yang dilakukan | Model | Hasil |
|---|---|---|---|
| 1. Bible | Storyboard disempurnakan menjadi bible: arah, cahaya, karakter, shot list | — | Bagus. Menjadi pegangan sampai akhir |
| 2. Referensi | Rafi, Adinda, toko, varian cahaya, figuran dari belakang | Nano Banana Pro (~$0.17/gbr) | Adinda dan toko masing-masing direvisi sekali (2 opsi, user memilih). Konsistensi wajah bagus |
| 3. Keyframe | 22 keyframe 9:16 | Nano Banana Pro multi-ref | Bagus. 3 shot direvisi (salah satunya karena cerita roti coklat diubah user) |
| 4. Video realistis | Tes 3 klip, lalu semua shot | Kling 3.0 1080p (~$0.40/klip) | Kualitas tinggi. 1 ulang karena senyum terlalu lebar. Rough cut v1 jadi |
| 5. Riset biaya | Gratis? Sewa GPU? MiniMax API? Provider gambar? | Wan 2.2 dites | Wan buruk dan mahal, ditolak. Kesimpulan: hibrida API langsung + ComfyUI untuk open-weights |
| 6. Pivot anime | Gaya anime 90-an; referensi ulang | Seedream 5.0 Flash | Gaya kuat, murah. Output selalu persegi |
| 7. Anime H3 | Tes klip terpisah vs multi-shot, lalu 9 adegan multi-shot | MiniMax H3 ref2v turbo | Efisien (22 shot jadi 9 generate) + audio. 608×1056. **9 adegan belum direview** |
| 8. Anime tanpa r2v | 3 keyframe Seedream, lalu Kling | Seedream + Kling 3.0 | Malam bersih; **pagi halusinasi**; sore wajah terlihat |
| 9. Dokumentasi | Bible, knowledge, repo | — | Kredit Comfy habis sebelum shot pagi/sore diulang |

## Yang berhasil
- **Bible sebagai pegangan tunggal.** Setiap revisi user masuk ke sana, sehingga prompt selalu bersumber dari satu tempat.
- **Dua opsi untuk aset kunci.** User cepat memutuskan, dan revisi tidak berputar-putar.
- **Tes 3 klip sebelum batch penuh** menangkap masalah prompt lebih awal dengan biaya kecil.
- **Figuran selalu dari belakang.** Masalah konsistensi wajah figuran hilang sama sekali.
- **Nano Banana Pro + Kling 3.0** untuk realistis: kombinasi yang stabil dan siap produksi.
- **H3 multi-shot:** satu generate menghasilkan beberapa shot dengan hard cut dan ambience, jauh lebih murah per detik.
- **Keyframe mengunci gaya:** Kling mempertahankan look cel anime dari keyframe Seedream dengan sangat baik.
- **Skrip kecil** (batch builder, rough cut, contact sheet) membuat semuanya bisa diulang.

## Yang gagal & penyebabnya
1. **Halusinasi objek di shot pagi (paling fatal).** Aku menulis "wipes his hand once on his apron". Kling tidak bisa memodelkan tangan yang menyentuh kain, jadi ia mengarang tangan masuk ke balik apron dan muncul kantong. **Penyebabnya prompt-ku, bukan semata modelnya.** Aksinya juga berlapis (geser nampan, lepas, lap tangan).
2. **Wajah figuran terlihat di shot sore.** Aku menulis "turns his head to look toward the kitchen door". Gerak kepala itu membuat profil wajahnya terlihat.
3. **Biaya produksi penuh realistis sebelum gaya final dikunci.** Sekitar $13+ untuk 22 keyframe dan 22 klip realistis, lalu proyek pivot ke anime. Kalau gaya dites lebih awal, sebagian besar biaya itu bisa diarahkan ke versi final.
4. **Ritme seragam.** Semua shot realistis 3–5 detik, sehingga user baru sadar belakangan bahwa durasi perlu bervariasi. Ritme seharusnya diputuskan di animatic, bukan setelah video jadi.
5. **Seedream selalu 1024×1024.** Aku baru sadar setelah keyframe dibuat. Seharusnya ukuran output dicek dari gambar pertama sebelum merencanakan semuanya.
6. **Terlalu banyak jalur terbuka bersamaan.** Jalur H3 belum direview ketika jalur Kling anime dimulai. Perhatian terpecah dan hasil H3 masih menggantung.
7. **Operasional:** sesi Comfy kedaluwarsa di tengah job; kredit habis di tengah eksperimen; `wait_for_batch` salah status. Aku juga tidak mencatat biaya berjalan, jadi saldo habis tanpa peringatan.
8. **Referensi YouTube tidak bisa dibuka agent.** Gaya diturunkan dari judulnya saja. Seharusnya aku langsung minta screenshot.

## Trade-off model yang terlihat
| Pilihan | Untung | Rugi |
|---|---|---|
| Nano Banana Pro vs Seedream Flash | NB: 9:16 native, wajah realistis kuat | NB ~4–5× lebih mahal. Seedream: murah, gaya ilustrasi kuat, tapi persegi |
| Kling 3.0 (keyframe) vs H3 (referensi) | Kling: 1080p, kontrol per shot, API langsung | Kling: 1 shot per generate, tanpa audio, ±3× biaya per film. H3: murah, multi-shot, audio, tapi resolusi rendah dan butuh GPU |
| Klip terpisah vs multi-shot | Terpisah: kontrol durasi tepat | Multi-shot: lebih murah dan transisinya terasa diedit, tapi timing meleset ±1 dtk |
| Comfy Cloud vs API langsung | Comfy: satu tempat, campur partner + open-weights | Sesi dan kredit jadi satu titik gagal; API langsung lebih stabil untuk produksi rutin |
| Resolusi tinggi sejak awal vs bertahap | Tinggi sejak awal: yang dilihat user = hasil akhir | Mahal kalau cerita atau gaya berubah, dan di proyek ini keduanya berubah |

## Refleksi: kalau diulang, aku akan…
Mengerjakannya **bertahap dengan gerbang persetujuan**. Setiap fase murah dan cepat, dan biaya naik hanya setelah fase sebelumnya dikunci:

| Fase | Output | Model/cara | Perkiraan biaya | Gerbang |
|---|---|---|---|---|
| 0. Brief | Bible v0 + pertanyaan kunci (gaya, durasi, referensi visual sebagai **gambar**) | Teks | 0 | User setuju arah |
| 1. Sketsa storyboard | 1 frame kasar per shot (sketsa pensil / grayscale) | Model gambar paling murah, resolusi rendah, atau sketsa HTML/SVG | <$1 | Cerita & komposisi dikunci |
| 2. Animatic | Frame sketsa disusun dengan durasi per shot + audio kasar | ffmpeg | 0 | **Ritme & durasi** dikunci |
| 3. Tes gaya | 1 shot kunci dalam 2–3 gaya (mis. realistis vs anime) | Model gambar + 1 klip video per gaya | ±$2 | **Gaya** dikunci |
| 4. Referensi | Karakter & lokasi final (2 opsi) | Model gambar terbaik untuk gaya terpilih | ±$1–2 | Wajah & lokasi dikunci |
| 5. Motion draft | Semua shot dalam gerak, resolusi rendah | H3 turbo 0.6 MP multi-shot / model video termurah | ±$3–6 | Aksi bebas halusinasi, blocking OK |
| 6. Final | Hanya shot yang lolos; keyframe hi-res → video 1080p, 2 versi untuk shot penting | NB/Seedream + Kling | ±$10–15 | QA lolos |
| 7. Edit | Rough cut, teks/UI mockup, sound | ffmpeg + HTML | 0 | User approve |

Hal lain:
- **Cek dulu ukuran dan format output** setiap model baru dari gambar pertama.
- **Buat buku besar biaya** per proyek (`manifest.json` atau tabel di README) dan cek saldo sebelum setiap batch.
- **Satu jalur dievaluasi tuntas** (contact sheet + laporan) sebelum membuka jalur baru.
- **Tulis prompt video seperti instruksi ke aktor:** satu aksi, apa yang tetap diam, tanpa interaksi tangan dengan benda kecil.
- **Minta referensi visual sebagai gambar,** bukan link video yang mungkin tidak bisa dibuka.

## Status yang ditinggalkan untuk agent berikutnya
- 9 adegan H3 sudah selesai di Comfy Cloud (job A1–A9), tinggal diunduh dan direview.
- Shot pagi/sore jalur Kling anime: prompt v2 siap di `project/invisible-mistakes/prompts/anime_keyframe_kling_test.json`; tunggu kredit diisi.
- Keputusan jalur anime final (H3 vs Kling vs hibrida) belum diambil user.

## Dipindah ke knowledge
- [x] Halusinasi & QA → `knowledge/05-qa-dan-halusinasi.md`
- [x] Pola prompt → `knowledge/04-prompting.md`
- [x] Pipeline bertahap → `knowledge/02-pipeline.md`
- [x] Model & quirk → `knowledge/03-model-dan-provider.md`, `08-comfy-cloud.md`
- [x] Biaya → `knowledge/06-biaya.md`
