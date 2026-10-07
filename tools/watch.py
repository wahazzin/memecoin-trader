"""
watch.py -- have Gemini actually WATCH a YouTube video (picture + sound) and write study notes.
Runs on GitHub (Gemini fetches the video on Google's side, so YouTube's block on cloud servers doesn't matter).
Usage: GEMINI_API_KEY=... python tools/watch.py <youtube-url> [focus question] [out_dir]
"""
import json
import os
import re
import sys
import time

import requests

API = "https://generativelanguage.googleapis.com/v1beta"
PROMPT = """You are studying a trading video for a team that builds AUTOMATED, paper-traded trading systems and
tests every rule before trusting it. Watch the whole video (screen AND audio). Write markdown notes:

1. **What's on screen** that the narration alone wouldn't tell: chart timeframes, indicator settings, the exact
   numbers in filter panels / holder tabs / settings screens, P&L screenshots (are wallet addresses or full
   histories shown, or just cropped wins?). Give timestamps (mm:ss).
2. **Every concrete rule** (entry, exit, filter, sizing) with its exact numbers, timestamp, and whether a
   bot could check it from data (yes / partly / no).
3. **Evidence quality**: what is actually proven on screen vs only claimed. Any sponsor, referral or paid group.
4. **Contradictions** with common sense or within the video.
Be precise and skeptical. Don't invent numbers that aren't shown or said. Focus: {focus}"""


def pick_model(key):
    pref = os.environ.get("GEMINI_MODEL")
    if pref:
        return pref
    js = requests.get(f"{API}/models", params={"key": key, "pageSize": 200}, timeout=30).json()
    names = [m["name"].split("/")[-1] for m in js.get("models", [])
             if "generateContent" in m.get("supportedGenerationMethods", [])]
    def score(n):                       # newest "flash" (free-tier friendly), not lite/image/tts/preview-exp
        if "flash" not in n or any(x in n for x in ("lite", "image", "tts", "audio", "live", "thinking", "exp")):
            return (-1,)
        v = re.findall(r"(\d+)\.(\d+)", n)
        return (int(v[0][0]), int(v[0][1]), "preview" not in n) if v else (0,)
    print("models available:", ", ".join(sorted(names)[:40]))
    if not names:
        raise SystemExit(f"model list failed: {json.dumps(js)[:600]}")
    ranked = sorted((n for n in names if score(n) != (-1,)), key=score, reverse=True)
    pros = sorted((n for n in names if "pro" in n and not any(x in n for x in ("image", "tts", "exp"))), reverse=True)
    return ranked[:4] + pros[:2] + ["gemini-3.8-flash"]


def watch(url, focus="all trading rules", out="research/out/watch"):
    key = os.environ["GEMINI_API_KEY"]
    models = pick_model(key)
    if isinstance(models, str):
        models = [models]
    body = {"contents": [{"parts": [{"file_data": {"file_uri": url, "mime_type": "video/*"}},
                                    {"text": PROMPT.format(focus=focus)}]}],
            "generationConfig": {"mediaResolution": "MEDIA_RESOLUTION_LOW", "temperature": 0.2}}
    tried = []
    for attempt in range(3):
        for model in dict.fromkeys(models):
            r = requests.post(f"{API}/models/{model}:generateContent", params={"key": key}, json=body, timeout=900)
            tried.append(f"{model}:{r.status_code}")
            if r.status_code == 200:
                break
            print("failed", model, r.status_code, r.text[:200])
        if r.status_code == 200:
            break
        time.sleep(45)
    print("tried:", tried)
    os.environ["WATCH_TRIED"] = ", ".join(tried)
    js = r.json()
    if r.status_code != 200:
        raise SystemExit(f"Gemini error {r.status_code}: {json.dumps(js)[:800]}")
    text = "".join(p.get("text", "") for p in js["candidates"][0]["content"]["parts"])
    usage = js.get("usageMetadata", {})
    vid = re.findall(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, f"{vid[0] if vid else 'video'}.md")
    with open(path, "w") as f:
        f.write(f"# Watched: {url}\n\nmodel `{model}` · tokens in {usage.get('promptTokenCount')} out "
                f"{usage.get('candidatesTokenCount')}\n\n{text}\n")
    print(open(path).read())
    return path


if __name__ == "__main__":
    a = sys.argv[1:]
    out_dir = a[2] if len(a) > 2 else "research/out/watch"
    try:
        watch(a[0], a[1] if len(a) > 1 and a[1] else "all trading rules", out_dir)
    except BaseException as e:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "ERROR.md"), "w") as f:
            f.write(f"# watch failed\n\n{type(e).__name__}: {e}\n\nkey present: {bool(os.environ.get('GEMINI_API_KEY'))}\n\ntried: {os.environ.get('WATCH_TRIED')}\n")
        raise
