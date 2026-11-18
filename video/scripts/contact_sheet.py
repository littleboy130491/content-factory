#!/usr/bin/env python3
"""Contact sheet untuk QA: N frame per klip, satu baris per klip.

Pakai:
  python3 contact_sheet.py out.jpg klip1.mp4 klip2.mp4 [--frames 4] [--width 300]

Lihat hasilnya frame demi frame dengan checklist knowledge/05-qa-dan-halusinasi.md.
Untuk halusinasi cepat (benda muncul sesaat), naikkan --frames ke 8-12.
"""
import argparse, subprocess, tempfile, os
from PIL import Image, ImageDraw


def duration(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).strip())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out"); ap.add_argument("clips", nargs="+")
    ap.add_argument("--frames", type=int, default=4); ap.add_argument("--width", type=int, default=300)
    a = ap.parse_args()
    rows = []
    tmp = os.path.join(tempfile.gettempdir(), "cs_frame.jpg")
    for c in a.clips:
        d = duration(c)
        ts = [0.1 + i * (d - 0.25) / max(1, a.frames - 1) for i in range(a.frames)]
        fr = []
        for t in ts:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", c, "-frames:v", "1",
                            "-vf", f"scale={a.width}:-2", tmp], check=True)
            fr.append((t, Image.open(tmp).copy()))
        rows.append((os.path.basename(c), fr))
    fh = rows[0][1][0][1].height + 18
    sheet = Image.new("RGB", (a.width * a.frames, fh * len(rows)), (18, 18, 18))
    dr = ImageDraw.Draw(sheet)
    for r, (name, fr) in enumerate(rows):
        for j, (t, im) in enumerate(fr):
            sheet.paste(im, (j * a.width, r * fh + 18))
            dr.text((j * a.width + 4, r * fh + 3), f"{name} @{t:.1f}s", fill=(255, 220, 0))
    sheet.save(a.out, quality=85)
    print("tulis", a.out)


if __name__ == "__main__":
    main()
