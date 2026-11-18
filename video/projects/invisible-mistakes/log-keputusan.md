# Log keputusan — Invisible Mistakes

Berurutan. Format: tanggal — keputusan (sumber).

## Brief & arah
- Nov 2026 — Storyboard PDF dari user disempurnakan menjadi bible. Arah: "short story dengan sinematografi bagus, bukan iklan"; natural, tidak terlihat AI; detail cahaya dan udara; konsistensi wajah dan ekspresi natural itu sangat penting. *(user)*
- Rafi ±20 th dan Adinda ±30 th, **keduanya orang Indonesia**. *(user)*

## Aset
- Adinda v1 ditolak: "harus lebih menarik dan lebih muda, lebih ramah". v2 dibuat 2 opsi, **B dipilih**. *(user)*
- Toko v1 ditolak: "bakery harus lebih real". v2 dibuat 2 opsi, **A dipilih**. *(user)*
- Varian cahaya pagi, siang, sore, dan malam dibuat dari toko v2-A.

## Cerita
- Roti coklat yang salah taruh "jangan terlalu obvious dekat". Dibuat adegan terpisah: ternyata ditaruh di rak berbeda yang agak jauh (reveal dengan rack focus). *(user)*

## Video realistis
- Kling 3.0, 1080p, tanpa audio, 3–5 dtk per shot. Tes 3 klip disetujui, lalu semua shot dijalankan.
- vid07: senyum Rafi terlalu lebar, diulang dengan "faint closed-lip smile, no teeth".
- Final keyframe yang direvisi: kf09v2, kf12v3, kf17v2.
- Rough cut v1 jadi (`prompts/realistic_edit.json`).

## Eksplorasi biaya & infrastruktur
- Ditanyakan: opsi gratis, sewa GPU (RunPod/Vast/RunComfy/Higgsfield), Comfy Cloud vs RunPod, MiniMax API, perbandingan provider gambar. *(user)*
- Tes Wan 2.2: kualitas buruk, lambat, mahal, sehingga ditolak.

## Pivot anime
- User meminta gaya **anime 90-an** dengan **Seedream Flash** dan workflow **MiniMax H3 ref2v turbo** miliknya. Referensinya sebuah YouTube Short (tidak bisa diakses dari agent). *(user)*
- Tes 3 klip, lalu user menyadari **durasi per klip perlu bervariasi**. Solusinya multi-shot per adegan dengan timing di prompt, lalu dirapikan saat trim. *(user menyetujui)*
- 9 adegan H3 dikirim (A1–A9).

## Orkestrasi
- User bertanya apakah ComfyUI masih perlu. Rekomendasinya hibrida: model partner lewat API langsung, ComfyUI hanya untuk open-weights (H3).
- User minta mencoba **tanpa reference-to-video**: keyframe Seedream + Kling. *(user)*
- Hasil tes: shot pagi **halusinasi** (tangan masuk apron, muncul kantong). User menilai ini "kesalahan paling fatal". Istilahnya: halusinasi objek / kesalahan logika-kontinuitas. Aturan pencegahan dimasukkan ke bible dan `knowledge/05`. *(user)*
- Ulang shot pagi/sore dengan prompt v2 disetujui, tapi **kredit Comfy habis**, jadi tertunda.
