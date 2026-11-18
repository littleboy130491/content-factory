#!/usr/bin/env python3
"""Menyusun item submit_batch Comfy untuk Kling 3.0 image-to-video (template `api_kling_v3_video`).

Input JSON:
  {"prefix": "(opsional, ditaruh di depan setiap prompt)",
   "suffix": "(opsional, ditaruh di belakang setiap prompt)",
   "negative": "negative prompt dasar",
   "shots": [{"name", "image": "<nama upload Comfy dari keyframe>", "duration": 3-10,
              "prompt", "seed", "negative_extra": "(opsional)"}]}

Pakai:
  python3 kling_batch.py shots.json -o items.json [--only vid07 vid12] [--audio] [--resolution 1080p]

Template ini tidak punya input frame akhir. Untuk start+end frame pakai API Kling langsung.
"""
import argparse, json


def item(shot, cfg, audio, resolution, aspect):
    prompt = " ".join(x for x in (cfg.get("prefix", ""), shot["prompt"], cfg.get("suffix", "")) if x).strip()
    neg = ", ".join(x for x in (cfg.get("negative", ""), shot.get("negative_extra", "")) if x)
    return {"tool": "run_template", "name": "api_kling_v3_video", "description": shot["name"],
            "input_overrides": {
                "1": {"image": shot["image"]},
                "3": {"multi_shot": "disabled", "multi_shot.prompt": prompt, "multi_shot.negative_prompt": neg,
                      "multi_shot.duration": int(shot["duration"]), "generate_audio": audio,
                      "model": "kling-v3", "model.resolution": resolution, "model.aspect_ratio": aspect,
                      "seed": shot.get("seed", 0)}}}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("shots"); ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--only", nargs="*"); ap.add_argument("--audio", action="store_true")
    ap.add_argument("--resolution", default="1080p"); ap.add_argument("--aspect", default="9:16")
    a = ap.parse_args()
    cfg = json.load(open(a.shots))
    shots = [s for s in cfg["shots"] if not a.only or s["name"] in a.only]
    items = [item(s, cfg, a.audio, a.resolution, a.aspect) for s in shots]
    json.dump(items, open(a.out, "w"))
    print(len(items), "item ->", a.out, "| total detik:", sum(int(s["duration"]) for s in shots))


if __name__ == "__main__":
    main()
