"""health.py -- are all bots alive? Uses only public GitHub data. Alerts to Discord when stale.
Alert state (last alert per problem) is kept in the `health-state` branch to avoid spamming."""
import json
import os
import subprocess
import time

import requests

from memebot import notify

API = "https://api.github.com"
H = {"Accept": "application/vnd.github+json"}
if os.environ.get("GH_TOKEN"):
    H["Authorization"] = f"Bearer {os.environ['GH_TOKEN']}"


def last_commit_age(repo, branch):
    js = requests.get(f"{API}/repos/{repo}/commits", headers=H, params={"sha": branch, "per_page": 1}, timeout=30).json()
    t = js[0]["commit"]["committer"]["date"]
    return time.time() - time.mktime(time.strptime(t, "%Y-%m-%dT%H:%M:%SZ")) + time.timezone * 0


def newest_release_asset_age(repo):
    rels = requests.get(f"{API}/repos/{repo}/releases", headers=H, params={"per_page": 2}, timeout=30).json()
    ts = [a["created_at"] for r in rels for a in r.get("assets", [])]
    if not ts:
        return 1e9
    t = max(ts)
    return time.time() - _utc(t)


def _utc(t):
    import calendar
    return calendar.timegm(time.strptime(t, "%Y-%m-%dT%H:%M:%SZ"))


def running(repo, wf):
    js = requests.get(f"{API}/repos/{repo}/actions/workflows/{wf}/runs", headers=H, params={"status": "in_progress"}, timeout=30).json()
    return js.get("total_count", 0)


def checks():
    out = []
    try:
        js = requests.get(f"{API}/repos/wahazzin/memecoin-trader/commits", headers=H,
                          params={"sha": "paper-state", "per_page": 1}, timeout=30).json()
        age = time.time() - _utc(js[0]["commit"]["committer"]["date"])
        if age > 40 * 60:
            out.append(("paperbot", f"Memecoin paper bot hasn't saved for {age / 60:.0f} min (expected every 5 min)."))
    except Exception as e:
        out.append(("paperbot", f"Couldn't read the paper bot state ({type(e).__name__})."))
    try:
        age = newest_release_asset_age("wahazzin/memecoin-trader")
        if age > 2.5 * 3600:
            out.append(("recorder", f"Memecoin recorder hasn't uploaded data for {age / 3600:.1f} h (expected hourly)."))
    except Exception as e:
        out.append(("recorder", f"Couldn't read recorder uploads ({type(e).__name__})."))
    try:
        # silent-failure check: the bot judges ~5 coins/minute. If pump.fun changes its program and our decoder
        # stops understanding trades, everything keeps "running" but no coin is ever judged.
        r = requests.get("https://raw.githubusercontent.com/wahazzin/memecoin-trader/paper-state/signals.jsonl",
                         headers={"Range": "bytes=-4000", "Accept-Encoding": "identity"}, timeout=30)   # no gzip: a byte range of a gzipped file cannot be decoded
        last = [l for l in r.text.splitlines() if l.startswith("{")]
        ts = json.loads(last[-1])["ts"] if last else 0
        if time.time() - ts > 2 * 3600:
            out.append(("decoder", f"Memecoin bot hasn't judged a single coin in {(time.time() - ts) / 3600:.1f} h "
                                   "(normally ~5 per minute). pump.fun may have changed its program or the data feed broke."))
    except Exception as e:
        out.append(("decoder", f"Couldn't read the bot's signals ({type(e).__name__})."))
    try:
        # early-warning tripwire on storage: the recorder adds ~250 MB/day of release files. GitHub has no
        # published total cap for releases, but very large repos can get flagged. Warn at 15 GB (~2 months),
        # well before it matters, with the projected date so there's time to compact old data.
        total, page, sizes = 0, 1, []
        while True:
            rels = requests.get(f"{API}/repos/wahazzin/memecoin-trader/releases", headers=H,
                                params={"per_page": 100, "page": page}, timeout=30).json()
            if not rels:
                break
            for r in rels:
                total += sum(a["size"] for a in r.get("assets", []))
            page += 1
        gb = total / 1e9
        if gb > 15:
            out.append(("storage", f"Memecoin recorder data is at {gb:.1f} GB (warning level 15 GB, ~250 MB/day). "
                                   "Time to compact old data: ask Claude to run the storage plan in RESEARCH_LOG.md."))
    except Exception as e:
        out.append(("storage", f"Couldn't measure recorder storage ({type(e).__name__})."))
    # the crypto AI trader has its own health check posting to its own channel (crypto-ai-trader/health.yml)
    return out


def main():
    problems = checks()
    state_dir = "health_state"
    url = f"https://x-access-token:{os.environ.get('GH_TOKEN', '')}@github.com/wahazzin/memecoin-trader.git"
    have = subprocess.run(["git", "clone", "-q", "--depth", "1", "--branch", "health-state", url, state_dir]).returncode == 0
    if not have:
        os.makedirs(state_dir, exist_ok=True)
        subprocess.run(["git", "-C", state_dir, "init", "-q"]); subprocess.run(["git", "-C", state_dir, "checkout", "-q", "-b", "health-state"])
        subprocess.run(["git", "-C", state_dir, "remote", "add", "origin", url])
    p = os.path.join(state_dir, "alerts.json")
    last = json.load(open(p)) if os.path.exists(p) else {}
    now = time.time()
    sent = []
    for key, msg in problems:
        if now - last.get(key, 0) > 6 * 3600:
            notify.send(f"⚠️ {msg} Paper only, no money at risk. I'll look into it when you next open the chat.")
            last[key] = now; sent.append(key)
    for key in list(last):
        if key not in [k for k, _ in problems] and last[key] > 0:
            notify.send(f"✅ Recovered: {key} is running again.")
            last[key] = 0
            sent.append(key)
    print("problems:", problems, "alerts sent:", sent)
    json.dump(last, open(p, "w"))
    subprocess.run(["git", "-C", state_dir, "-c", "user.name=memebot", "-c", "user.email=actions@github.com", "add", "-A"])
    subprocess.run(["git", "-C", state_dir, "-c", "user.name=memebot", "-c", "user.email=actions@github.com", "commit", "-q", "-m", "health"])
    subprocess.run(["git", "-C", state_dir, "push", "-q", "origin", "HEAD:health-state"])


if __name__ == "__main__":
    main()
