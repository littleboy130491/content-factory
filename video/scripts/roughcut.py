#!/usr/bin/env python3
"""Rough cut: normalisasi setiap klip, trim, lalu gabungkan.

Input JSON (edit list):
  {"output": "film_roughcut_v1.mp4",
   "width": 1080, "height": 1920, "fps": 24, "grain": 6, "anime_twos": false, "keep_audio": false,
   "clips": [{"shot": "01", "file": "vid01.mp4", "start": 0, "seconds": 4}]}

Pakai:
  python3 roughcut.py edit.json --dir path/ke/klip

- Semua klip diskalakan dan di-crop ke ukuran target, fps disamakan, dan diberi grain tipis yang sama
  supaya hasil dari berbagai model menyatu.
- anime_twos=true menurunkan gerak ke 12 fps (rasa animasi "on twos") lalu kembali ke 24 fps.
- keep_audio=true mempertahankan audio klip (mis. output MiniMax H3); klip tanpa audio diberi audio hening.
"""
import argparse, json, os, subprocess


def has_audio(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
                          "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip()
    return bool(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edit"); ap.add_argument("--dir", default=".")
    a = ap.parse_args()
    e = json.load(open(a.edit))
    W, H, fps = e.get("width", 1080), e.get("height", 1920), e.get("fps", 24)
    grain, twos, keep_audio = e.get("grain", 6), e.get("anime_twos", False), e.get("keep_audio", False)
    norm = os.path.join(a.dir, "norm"); os.makedirs(norm, exist_ok=True)
    parts = []
    for c in e["clips"]:
        src = os.path.join(a.dir, c["file"])
        if not os.path.exists(src):
            print("hilang:", c["file"]); continue
        out = os.path.join(norm, f"{c['shot']}.mp4")
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
        vf += ("fps=12," if twos else "") + f"fps={fps},"
        vf += (f"noise=alls={grain}:allf=t," if grain else "") + "format=yuv420p"
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(c.get("start", 0)), "-t", str(c["seconds"]), "-i", src]
        if keep_audio and not has_audio(src):
            cmd += ["-f", "lavfi", "-t", str(c["seconds"]), "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v", "-map", "1:a"]
        cmd += ["-vf", vf]
        cmd += (["-c:a", "aac", "-ar", "48000", "-ac", "2"] if keep_audio else ["-an"])
        cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", out]
        subprocess.run(cmd, check=True)
        parts.append(out)
    lst = os.path.join(norm, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{os.path.abspath(p)}'\n" for p in parts)
    final = os.path.join(a.dir, e.get("output", "roughcut.mp4"))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", final], check=True)
    print("selesai:", final, len(parts), "klip")


if __name__ == "__main__":
    main()
