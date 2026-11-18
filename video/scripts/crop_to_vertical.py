#!/usr/bin/env python3
"""Crop gambar persegi (mis. output Seedream yang selalu 1024x1024) ke 9:16 lalu resize.

Pakai:
  python3 crop_to_vertical.py in.png out.png --x 220            # x = tepi kiri crop, ikuti posisi subjek
  python3 crop_to_vertical.py in.png out.png --center           # crop tengah

Default target 1080x1920. Cek dulu: subjek utama dan semua tokoh harus masuk ke jendela crop.
"""
import argparse
from PIL import Image

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("src"); ap.add_argument("dst")
ap.add_argument("--x", type=int); ap.add_argument("--center", action="store_true")
ap.add_argument("--size", default="1080x1920")
a = ap.parse_args()
im = Image.open(a.src).convert("RGB")
W, H = im.size
cw = round(H * 9 / 16)
x = (W - cw) // 2 if a.center or a.x is None else max(0, min(a.x, W - cw))
tw, th = map(int, a.size.split("x"))
im.crop((x, 0, x + cw, H)).resize((tw, th), Image.LANCZOS).save(a.dst)
print(f"crop x={x}..{x+cw} dari {W}x{H} -> {tw}x{th}: {a.dst}")
