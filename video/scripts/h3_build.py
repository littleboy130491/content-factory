#!/usr/bin/env python3
"""Membangun graph API ComfyUI untuk MiniMax H3 reference-to-video turbo, satu graph per adegan.

Input  : file JSON adegan dengan bentuk
         {"style": "...", "refs": {"key": {"image": "<nama upload Comfy>", "desc": "..."}},
          "scenes": [{"name", "seed", "duration", "refs": [keys], "body"}]}
Output : JSON list item untuk submit_batch Comfy (tool "submit_workflow"), atau satu graph per file.

Pakai:
  python3 h3_build.py scenes.json -o items.json            # semua adegan
  python3 h3_build.py scenes.json --only A2_keluarga -o a2.json
  python3 h3_build.py scenes.json --graphs-dir graphs/     # satu file graph per adegan

Catatan:
- Template bawaan `video_minimax_h3_r2v` hanya punya 2 slot referensi. Node
  MiniMaxH3ReferenceToVideo menerima sampai 9 (ref_images.ref_image_N); skrip ini membangun graph penuhnya.
- Panjang frame mengikuti aturan model: f = max(5, round(detik*24)); f += (5 - f % 17) % 17.
  Rentang latih kira-kira 124-362 frame (5-15 detik).
"""
import argparse, copy, json, os

BASE = {
 "92":{"class_type":"SaveVideo","inputs":{"filename_prefix":"video/MiniMax_H3","format":"auto","format.codec":"auto","video":["130",0]}},
 "115":{"class_type":"ResolutionSelector","inputs":{"aspect_ratio":"9:16 (Portrait Widescreen)","megapixels":0.6,"multiple":32,"preview":""}},
 "119":{"class_type":"VAELoader","inputs":{"vae_name":"minimax_h3_video_vae_int8_convrot.safetensors"}},
 "120":{"class_type":"VAELoader","inputs":{"vae_name":"minimax_h3_audio_vae_fp32.safetensors"}},
 "121":{"class_type":"VAEDecodeAudio","inputs":{"samples":["125",0],"vae":["120",0]}},
 "122":{"class_type":"VAEDecode","inputs":{"samples":["125",0],"vae":["119",0]}},
 "123":{"class_type":"KSamplerSelect","inputs":{"sampler_name":"res_multistep"}},
 "124":{"class_type":"BasicScheduler","inputs":{"denoise":1,"model":["127",0],"scheduler":"simple","steps":4}},
 "125":{"class_type":"SamplerCustomAdvanced","inputs":{"guider":["126",0],"latent_image":["136",1],"noise":["129",0],"sampler":["123",0],"sigmas":["124",0]}},
 "126":{"class_type":"BasicGuider","inputs":{"conditioning":["136",0],"model":["145",0]}},
 "127":{"class_type":"UNETLoader","inputs":{"unet_name":"minimax_h3_ref2va_pruned_int8_convrot.safetensors","weight_dtype":"default"}},
 "128":{"class_type":"CLIPLoader","inputs":{"clip_name":"qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors","device":"default","type":"minimax"}},
 "129":{"class_type":"RandomNoise","inputs":{"noise_seed":1}},
 "130":{"class_type":"CreateVideo","inputs":{"audio":["121",0],"bit_depth":8,"fps":24,"images":["122",0]}},
 "136":{"class_type":"MiniMaxH3ReferenceToVideo","inputs":{"audio_vae":["120",0],"clip":["128",0],"height":["115",1],"length":124,"prompt":"","ref_image_size":"match","vae":["119",0],"width":["115",0]}},
 "145":{"class_type":"LoraLoaderModelOnly","inputs":{"lora_name":"minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors","model":["127",0],"strength_model":1}},
}
AUDIO_END = "\n\nNo music. No dialogue; mouths stay closed."


def frames_for(seconds):
    f = max(5, round(seconds * 24))
    return f + (5 - f % 17) % 17


def build(style, refs, scene, megapixels=0.6, aspect="9:16 (Portrait Widescreen)"):
    if len(scene["refs"]) > 9:
        raise ValueError(f"{scene['name']}: maksimal 9 referensi")
    wf = copy.deepcopy(BASE)
    wf["115"]["inputs"].update(megapixels=megapixels, aspect_ratio=aspect)
    wf["129"]["inputs"]["noise_seed"] = scene["seed"]
    wf["136"]["inputs"]["length"] = frames_for(scene["duration"])
    tags = []
    for i, key in enumerate(scene["refs"]):
        nid = str(200 + i)
        wf[nid] = {"class_type": "LoadImage", "inputs": {"image": refs[key]["image"]}}
        wf["136"]["inputs"][f"ref_images.ref_image_{i}"] = [nid, 0]
        tags.append(f"<Picture {i+1}> is {refs[key]['desc']}")
    body = scene["body"]
    if "No dialogue" not in body:
        body += AUDIO_END
    wf["136"]["inputs"]["prompt"] = (style.strip() + " " + "; ".join(tags) +
        ". Keep every character and the room exactly as in their references across all shots.\n\n" + body)
    return wf


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scenes")
    ap.add_argument("-o", "--out", help="tulis list item submit_batch ke file ini")
    ap.add_argument("--only", nargs="*", help="nama adegan yang dibangun")
    ap.add_argument("--graphs-dir", help="tulis satu graph per adegan ke folder ini")
    ap.add_argument("--megapixels", type=float, default=0.6)
    a = ap.parse_args()
    data = json.load(open(a.scenes))
    scenes = [s for s in data["scenes"] if not a.only or s["name"] in a.only]
    items = []
    for s in scenes:
        wf = build(data["style"], data["refs"], s, a.megapixels)
        items.append({"tool": "submit_workflow", "description": s["name"], "workflow": wf})
        if a.graphs_dir:
            os.makedirs(a.graphs_dir, exist_ok=True)
            json.dump(wf, open(os.path.join(a.graphs_dir, s["name"] + ".json"), "w"), indent=1)
        print(f"{s['name']:24s} {s['duration']:>5}s  {frames_for(s['duration'])} frame  refs={s['refs']}")
    if a.out:
        json.dump(items, open(a.out, "w"))
        print("tulis", a.out, len(items), "item")


if __name__ == "__main__":
    main()
