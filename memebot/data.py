"""Load recorded data from the GitHub Releases ("data-YYYY-MM-DD") into pandas, de-duplicated by signature."""
import glob
import io
import os
import tarfile

import requests

API = "https://api.github.com"


def download(repo, dest, token=None, since=None):
    """Download every recorder tar into dest/ (skips files already there)."""
    os.makedirs(dest, exist_ok=True)
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    page = 1
    while True:
        rels = requests.get(f"{API}/repos/{repo}/releases", headers=h, params={"per_page": 100, "page": page}, timeout=60).json()
        if not rels:
            break
        for r in rels:
            if not r["tag_name"].startswith("data-") or (since and r["tag_name"][5:] < since):
                continue
            for a in r["assets"]:
                out = os.path.join(dest, a["name"])
                if os.path.exists(out):
                    continue
                b = requests.get(a["url"], headers={**h, "Accept": "application/octet-stream"}, timeout=600).content
                with open(out, "wb") as f:
                    f.write(b)
        page += 1


def load(dest, kinds=("creates", "trades", "events")):
    """Read every tar in dest/ -> {kind: DataFrame} plus 'gaps' (list) and 'status' (list)."""
    import json
    import pandas as pd
    import pyarrow.parquet as pq
    parts = {k: [] for k in kinds}
    gaps, status = [], []
    for tf in sorted(glob.glob(os.path.join(dest, "*.tar"))):
        with tarfile.open(tf) as t:
            for m in t.getmembers():
                name = os.path.basename(m.name)
                if name.startswith("status_"):
                    s = json.load(t.extractfile(m)); status.append(s); gaps += s.get("gaps", [])
                    continue
                k = name.split("_")[0]
                if k in parts and name.endswith(".parquet"):
                    parts[k].append(pq.read_table(io.BytesIO(t.extractfile(m).read())).to_pandas())
    out = {}
    for k, v in parts.items():
        df = pd.concat(v, ignore_index=True) if v else pd.DataFrame()
        if k == "trades" and len(df):
            df = df.drop_duplicates("sig").sort_values(["slot", "ts"]).reset_index(drop=True)
        if k == "creates" and len(df):
            df = df.drop_duplicates("mint").reset_index(drop=True)
        out[k] = df
    out["gaps"], out["status"] = gaps, status
    return out
