#!/usr/bin/env python3
"""Tamag06 ComfyUI helper — queue a workflow, wait, save images. Stdlib only.

  python tools/comfyui/comfy_gen.py --check
  python tools/comfyui/comfy_gen.py --workflow tools/comfyui/workflows/txt2img_basic.json \
      --checkpoint sd_xl_base_1.0.safetensors --positive "..." --out Assets/Art/_inbox/my_asset

Workflows must be exported from ComfyUI with "Save (API Format)". Placeholders such as
{{POSITIVE}} {{NEGATIVE}} {{SEED}} {{WIDTH}} {{HEIGHT}} {{BATCH}} {{STEPS}} {{CFG}}
{{CHECKPOINT}} {{PREFIX}} are substituted anywhere in the JSON. A value that is exactly
"{{SEED}}" (etc.) becomes a number, not a string.
"""
import argparse, json, os, random, sys, time, uuid
import urllib.parse, urllib.request, urllib.error

URL = os.environ.get("COMFY_URL", "http://127.0.0.1:8188").rstrip("/")
NUMERIC = {"SEED", "WIDTH", "HEIGHT", "BATCH", "STEPS", "CFG"}


def http(path, data=None, timeout=30):
    req = urllib.request.Request(URL + path, data=data,
                                 headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def checkpoints():
    info = json.loads(http("/object_info/CheckpointLoaderSimple"))
    spec = info["CheckpointLoaderSimple"]["input"]["required"]["ckpt_name"]
    # Old format: [[names...]]; newer: ["COMBO", {"options": [...]}]
    if isinstance(spec[0], list):
        return spec[0]
    if len(spec) > 1 and isinstance(spec[1], dict):
        return spec[1].get("options", [])
    return []


def substitute(node, values):
    if isinstance(node, dict):
        return {k: substitute(v, values) for k, v in node.items()}
    if isinstance(node, list):
        return [substitute(v, values) for v in node]
    if isinstance(node, str):
        for key, val in values.items():
            tok = "{{%s}}" % key
            if node == tok:
                return val if key in NUMERIC else str(val)
            if tok in node:
                node = node.replace(tok, str(val))
    return node


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true", help="ping ComfyUI and list checkpoints")
    p.add_argument("--workflow")
    p.add_argument("--positive", default="")
    p.add_argument("--negative", default="photo, 3d render, anime, cartoon, glossy, clean lineart, "
                                            "text, watermark, extra fingers, deformed hands")
    p.add_argument("--checkpoint", default=os.environ.get("COMFY_CHECKPOINT", ""))
    p.add_argument("--width", type=int, default=832)
    p.add_argument("--height", type=int, default=1216)
    p.add_argument("--batch", type=int, default=4)
    p.add_argument("--steps", type=int, default=30)
    p.add_argument("--cfg", type=float, default=6.5)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--out", help="output folder, e.g. Assets/Art/_inbox/<asset_id>")
    p.add_argument("--timeout", type=int, default=600, help="seconds to wait for the job")
    a = p.parse_args()

    try:
        ckpts = checkpoints()
    except (urllib.error.URLError, OSError) as e:
        sys.exit(f"ComfyUI not reachable at {URL} ({e}). Start ComfyUI or set COMFY_URL.")

    if a.check:
        print(f"ComfyUI OK at {URL}\nCheckpoints:")
        for c in ckpts:
            print("  " + c)
        return

    if not (a.workflow and a.out and a.positive):
        sys.exit("--workflow, --positive and --out are required (or use --check)")
    if a.checkpoint and ckpts and a.checkpoint not in ckpts:
        sys.exit(f"Checkpoint '{a.checkpoint}' not found. Available: {', '.join(ckpts)}")

    seed = a.seed if a.seed is not None else random.randint(0, 2**32 - 1)
    prefix = "tamag06_" + os.path.basename(os.path.normpath(a.out))
    values = {"POSITIVE": a.positive, "NEGATIVE": a.negative, "SEED": seed,
              "WIDTH": a.width, "HEIGHT": a.height, "BATCH": a.batch, "STEPS": a.steps,
              "CFG": a.cfg, "CHECKPOINT": a.checkpoint, "PREFIX": prefix}

    with open(a.workflow, encoding="utf-8") as f:
        wf = substitute(json.load(f), values)
    leftover = [k for k in values if "{{%s}}" % k in json.dumps(wf)]
    if not a.checkpoint and "{{CHECKPOINT}}" in open(a.workflow, encoding="utf-8").read():
        sys.exit("Workflow needs --checkpoint (run --check to list them)")
    if leftover:
        sys.exit(f"Unsubstituted placeholders: {leftover}")

    body = json.dumps({"prompt": wf, "client_id": str(uuid.uuid4())}).encode()
    try:
        pid = json.loads(http("/prompt", body))["prompt_id"]
    except urllib.error.HTTPError as e:
        sys.exit(f"ComfyUI rejected the workflow: {e.read().decode(errors='replace')}")
    print(f"queued {pid} (seed {seed})", flush=True)

    deadline = time.time() + a.timeout
    hist = None
    while time.time() < deadline:
        h = json.loads(http(f"/history/{pid}"))
        if pid in h:
            hist = h[pid]
            break
        time.sleep(2)
    if hist is None:
        sys.exit(f"Timed out after {a.timeout}s waiting for {pid}")
    status = hist.get("status", {})
    if status.get("status_str") == "error":
        sys.exit("ComfyUI job failed: " + json.dumps(status.get("messages", []))[:2000])

    os.makedirs(a.out, exist_ok=True)
    saved = []
    for node_out in hist.get("outputs", {}).values():
        for img in node_out.get("images", []):
            if img.get("type") != "output":
                continue
            q = urllib.parse.urlencode({k: img.get(k, "") for k in ("filename", "subfolder", "type")})
            data = http("/view?" + q, timeout=120)
            dest = os.path.join(a.out, f"{seed}_{len(saved):02d}.png")
            with open(dest, "wb") as f:
                f.write(data)
            saved.append(dest)

    meta = {"positive": a.positive, "negative": a.negative, "seed": seed, "checkpoint": a.checkpoint,
            "workflow": a.workflow, "width": a.width, "height": a.height, "steps": a.steps,
            "cfg": a.cfg, "batch": a.batch, "files": [os.path.basename(s) for s in saved],
            "created": time.strftime("%Y-%m-%d %H:%M:%S")}
    log = os.path.join(a.out, "prompt.json")
    runs = []
    if os.path.exists(log):
        try:
            runs = json.load(open(log, encoding="utf-8"))
        except ValueError:
            runs = []
    runs.append(meta)
    with open(log, "w", encoding="utf-8") as f:
        json.dump(runs, f, ensure_ascii=False, indent=2)

    print(f"saved {len(saved)} image(s):")
    for s in saved:
        print("  " + s)


if __name__ == "__main__":
    main()
