# Video — produksi film pendek AI

Basis pengetahuan, template, dan skrip untuk membuat film pendek dengan AI (gambar → video → edit). AI agent: baca [`AGENTS.md`](AGENTS.md) (atau [`CLAUDE.md`](CLAUDE.md) untuk Claude) lebih dulu.

```
video/
├── AGENTS.md            aturan untuk semua AI agent
├── CLAUDE.md            AGENTS.md + catatan khusus Claude
├── knowledge/           pengetahuan GLOBAL (berlaku untuk semua proyek)
│   ├── 01-prinsip-dan-gaya.md
│   ├── 02-pipeline.md          ← termasuk alur bertahap murah → mahal
│   ├── 03-model-dan-provider.md
│   ├── 04-prompting.md
│   ├── 05-qa-dan-halusinasi.md
│   ├── 06-biaya.md
│   ├── 07-infrastruktur-dan-orkestrasi.md
│   ├── 08-comfy-cloud.md
│   └── 09-pasca-produksi.md
├── diary/               catatan eksperimen & refleksi per proyek
├── templates/           bible, README proyek, entri diary, prompt
├── scripts/             h3_build, kling_batch, roughcut, contact_sheet, crop_to_vertical
├── workflows/           workflow ComfyUI (MiniMax H3 ref2v turbo)
└── projects/            pengetahuan KHUSUS proyek (dibuka hanya jika diminta)
    └── invisible-mistakes/
```

## Mulai proyek baru
1. Baca `diary/README.md`, bagian "Pelajaran terpenting".
2. `mkdir projects/<nama>`, lalu salin `templates/project-readme.md` dan `templates/bible.md`.
3. Ikuti fase di `knowledge/02-pipeline.md`.
4. Di akhir, tulis entri diary dan pindahkan pelajaran umum ke `knowledge/`.

## Kebutuhan skrip
Python 3 + Pillow, ffmpeg/ffprobe. Contoh pemakaian ada di docstring tiap skrip (`python3 scripts/<skrip>.py -h`).
