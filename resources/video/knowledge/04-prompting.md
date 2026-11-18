# 04 — Prompting

## Struktur prompt keyframe (gambar)
```
[format & gaya] + [Image N is … untuk tiap referensi, sebut "keep his face / keep its layout"]
+ [waktu & cahaya & udara] + [ukuran shot + subjek + aksi diam + ekspresi] + [suasana]
```
- Sebut setiap referensi dengan perannya: "Image 1 is the bakery interior (keep its layout exactly: …). Image 2 is the young baker (keep his face, short messy black hair, …)."
- Cahaya ditulis konkret: "low warm sunlight streams through the glass storefront in long beams with dust in the air".
- Ekspresi ditulis kecil dan spesifik: "calm focused face", "worried but calm".

## Struktur prompt video (image-to-video)
```
[prefix gaya, mis. "keep the exact hand-painted cel look"] + [kamera] + [SATU aksi sederhana] + [apa yang TIDAK bergerak] + [udara]
```
- **Kamera dulu:** "Locked-off camera", "Very slow push-in", "Slow rack focus".
- **Satu aksi, kata kerja sederhana:** meletakkan, menoleh pelan, berkedip, berjalan keluar.
- **Tulis yang harus diam:** "The bread and price cards stay exactly as they are." Ini mengurangi halusinasi.
- **Tokoh yang membelakangi:** "stands still with his back to the camera; does not turn around". Jangan menulis "turns his head", karena model akan memperlihatkan profil.
- **Senyum:** "faint closed-lip smile, does not show teeth" + negative `wide grin`.

## Struktur prompt multi-shot (H3)
```
STYLE + "<Picture 1> is …; <Picture 2> is …. Keep every character and the room exactly as in their references across all shots."

[waktu/cahaya]. Hard cuts between shots.
Shot 1 | 0-3.5s: [ukuran shot + kamera + aksi]
Shot 2 | 3.5-6.5s: Hard cut. […]
Audio: [ambience + foley]

No music. No dialogue; mouths stay closed.
```
- 2–4 shot per generate, total 5–12 dtk. Variasikan panjang shot di timing.
- Satu adegan = satu waktu/cahaya. Jangan campur pagi dan malam dalam satu generate.

## Negative prompt standar
Lihat `templates/prompts/negative.txt`. Selalu sertakan:
`new objects appearing, objects disappearing, hands entering clothes, face morphing, identity change, extra fingers, talking, lip movement, looking at camera, text, watermark`.
Untuk anime tambah: `3D render, CGI, glossy modern anime, photorealistic`. Untuk realistis tambah: `cartoon, CGI, plastic skin`.

## Yang harus dihindari di prompt
| Hindari | Kenapa | Ganti dengan |
|---|---|---|
| Interaksi tangan dengan kain/saku/bungkus ("wipes his hand on his apron") | Memicu halusinasi objek | Aksi lepas: "lets go of the tray and stays still" |
| Aksi berlapis dalam satu shot ("slides, lets go, wipes, turns") | Model mengarang transisi | Pecah jadi beberapa shot |
| "turns his head" untuk figuran | Wajah/profil terlihat | "stands still, only shoulders rise with a breath" |
| Teks spesifik di benda | Huruf jadi acak | Kartu teks di edit, atau mockup |
