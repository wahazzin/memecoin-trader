"""
stream.py -- day-by-day loader for M1/M2/W1 (amendment "B-data", 2026-11-23, written before any test ran).

Why: the old loader (memebot/data.load + m1.from_recordings) downloaded all ~22 GB of recordings and turned every
trade into a Python dict at once -> a GitHub runner (14 GB disk, 16 GB RAM) cannot hold it. And its gap rule used the
recorder's LOGGED reconnect events (12k+ a week, mostly harmless 1-2 s reconnects of one of three streams), which
would have excluded most coins for a logging reason.

What this does instead (rules fixed in research/M1_PREREG.md, M2_PREREG.md, W1_PREREG.md "Amendment B-data"):
- Downloads one UTC day at a time (+ the last hour of the day before and the first 2 hours of the day after, so every
  coin's 100-minute window is complete), processes it, and deletes files that the next day no longer needs.
- Coins are those CREATED on that day (and >= 2026-10-07 20:45 UTC, the M1 A1 start; <= END_DAY).
- Outages are measured from the merged, de-duplicated data itself, not from the reconnect log:
    * bonding-curve stream: any interval > CURVE_SILENCE_S with no recorded pump.fun curve trade (whole market;
      the recorder sees ~8 curve trades per second, so 30 s of silence is an outage, not a lull);
    * PumpSwap stream: any interval > SWAP_SILENCE_S with no recorded PumpSwap trade.
  A coin is excluded if its window [created - 60 s, created + 6000 s] overlaps a curve outage, or overlaps a PumpSwap
  outage while the coin got near graduation (max curve vsol >= GRAD_NEAR_VSOL), because then its post-graduation
  trades may be missing.
- Everything else is exactly the old from_recordings(): non-SOL coins out (A2), rows with vsol/vtok <= 0 out,
  trades de-duplicated by signature and sorted by (slot, ts), coin = {mint, created, creator, trades}.
Order: chronological by day, then by mint (seeded random draws depend on order; the old loader used global mint
order. Seeds, rules and thresholds are unchanged).
"""
import glob
import io
import json
import os
import re
import shutil
import tarfile
from datetime import date, datetime, timedelta, timezone

import requests

API = "https://api.github.com"
START_TS = int(datetime(2026, 10, 7, 20, 45, tzinfo=timezone.utc).timestamp())
END_DAY = date(2026, 11, 22)              # last full UTC day before the amendment; fixed now
CURVE_SILENCE_S = 30
SWAP_SILENCE_S = 120
GRAD_NEAR_VSOL = 100.0                    # curve completes at ~115 virtual SOL (85 real + 30 virtual)
PRE_S, POST_S = 60, 6000
NAME = re.compile(r"rec_(\d{4}-\d{2}-\d{2})_(\d{2})_")


def list_assets(repo, token=None):
    """[(day, hour, name, api_url)] for every recorder tar."""
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    out, page = [], 1
    while True:
        rels = requests.get(f"{API}/repos/{repo}/releases", headers=h, params={"per_page": 100, "page": page},
                            timeout=60).json()
        if not rels:
            break
        for r in rels:
            if not r["tag_name"].startswith("data-"):
                continue
            for a in r["assets"]:
                m = NAME.match(a["name"])
                if m:
                    out.append((date.fromisoformat(m.group(1)), int(m.group(2)), a["name"], a["url"]))
        page += 1
    return sorted(out)


def _hour_ts(d, hr):
    return int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp()) + 3600 * hr


def files_for_day(assets, d):
    """Assets whose hour folder lies in [d-1 23:00, d+1 02:00)."""
    lo, hi = _hour_ts(d, 0) - 3600, _hour_ts(d, 0) + 26 * 3600
    return [a for a in assets if lo <= _hour_ts(a[0], a[1]) < hi]


def fetch(asset, dest, token=None):
    out = os.path.join(dest, asset[2])
    if not os.path.exists(out):
        h = {"Accept": "application/octet-stream"}
        if token:
            h["Authorization"] = f"Bearer {token}"
        with requests.get(asset[3], headers=h, timeout=600, stream=True) as r:
            r.raise_for_status()
            with open(out + ".part", "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
        os.replace(out + ".part", out)
    return out


TRADE_COLS = ["ts", "mint", "user", "buy", "sol", "tok", "vsol", "vtok", "fee_total_bps", "fee_bps", "cfee_bps",
              "venue", "slot", "sig", "price", "quote_mint", "fee", "cfee"]


def read_tars(paths):
    """-> (trades DataFrame, creates DataFrame, logged gaps list). Only the kinds/columns the tests need; strings
    become categoricals (one copy per distinct mint/wallet) so a busy October day fits a runner."""
    import pandas as pd
    import pyarrow as pa
    import pyarrow.parquet as pq
    tr, cr, gaps = [], [], []
    for p in paths:
        with tarfile.open(p) as t:
            for m in t.getmembers():
                name = os.path.basename(m.name)
                if name.startswith("status_"):
                    gaps += json.load(t.extractfile(m)).get("gaps", [])
                elif name.startswith("trades_") and name.endswith(".parquet"):
                    tb = pq.read_table(io.BytesIO(t.extractfile(m).read()))
                    tr.append(tb.select([c for c in TRADE_COLS if c in tb.column_names]))
                elif name.startswith("creates_") and name.endswith(".parquet"):
                    cr.append(pq.read_table(io.BytesIO(t.extractfile(m).read()),
                                            columns=["ts", "mint", "creator"]).to_pandas())
    if tr:
        tb = pa.concat_tables(tr, promote_options="permissive")
        del tr
        trades = tb.to_pandas(strings_to_categorical=True)
        del tb
        trades = trades.drop_duplicates("sig").sort_values(["slot", "ts"], kind="stable").reset_index(drop=True)
        trades = trades.drop(columns=["sig"])
    else:
        trades = pd.DataFrame()
    creates = pd.concat(cr, ignore_index=True) if cr else pd.DataFrame(columns=["ts", "mint", "creator"])
    if len(creates):
        creates = creates.drop_duplicates("mint").reset_index(drop=True)
    return trades, creates, gaps


def silences(ts_values, span_lo, span_hi, limit):
    """Intervals (a, b) longer than `limit` seconds with no event, inside [span_lo, span_hi] (edges count)."""
    ts = sorted(set(int(x) for x in ts_values if span_lo <= x <= span_hi))
    pts = [span_lo] + ts + [span_hi]
    return [(a, b) for a, b in zip(pts, pts[1:]) if b - a > limit]


def overlaps(lo, hi, intervals):
    return any(a < hi and b > lo for a, b in intervals)


def coins_from_frames(trades, creates, born_lo, born_hi, span_lo, span_hi, stats=None):
    """Yields coins created in [born_lo, born_hi) from one loaded span [span_lo, span_hi] (tested on synthetic
    frames). Outage rule: see module docstring."""
    stats = stats if stats is not None else {}
    if not len(trades):
        return
    tr = trades
    if "quote_mint" in tr.columns:
        from memebot.decode import SOL_MINTS
        bad = set(tr.loc[tr.quote_mint.notna() & ~tr.quote_mint.isin(SOL_MINTS), "mint"])
        tr = tr[~tr.mint.isin(bad)]                      # coins not priced in SOL are excluded (prereg A2)
    tr = tr[(tr.vsol > 0) & (tr.vtok > 0)]
    curve_mask = tr.venue.isna() if "venue" in tr.columns else tr.vsol == tr.vsol
    curve_out = silences(tr.loc[curve_mask, "ts"], span_lo, span_hi, CURVE_SILENCE_S)
    swap_out = silences(tr.loc[~curve_mask, "ts"], span_lo, span_hi, SWAP_SILENCE_S)
    stats["curve_outages"] = stats.get("curve_outages", 0) + len(curve_out)
    stats["swap_outages"] = stats.get("swap_outages", 0) + len(swap_out)
    stats["curve_outage_s"] = stats.get("curve_outage_s", 0) + sum(b - a for a, b in curve_out)
    born = creates[(creates.ts >= max(born_lo, START_TS)) & (creates.ts < born_hi)]
    creator = dict(zip(born.mint.astype(str), born.creator.astype(str)))
    created = dict(zip(born.mint.astype(str), born.ts.astype(int)))
    sub = tr[tr.mint.astype(str).isin(created)]
    drop = [c for c in sub.columns if c not in TRADE_COLS]
    if drop:
        sub = sub.drop(columns=drop)
    cm = curve_mask.loc[sub.index]
    groups = sub.groupby(sub.mint.astype(str), sort=True, observed=True).indices
    for mint in sorted(groups):
        idx = groups[mint]
        g = sub.iloc[idx]
        c0 = created[mint]
        lo, hi = c0 - PRE_S, c0 + POST_S
        if overlaps(lo, hi, curve_out):
            stats["excluded_curve_outage"] = stats.get("excluded_curve_outage", 0) + 1
            continue
        gc = g[cm.iloc[idx].values]
        if len(gc) and gc.vsol.max() >= GRAD_NEAR_VSOL and overlaps(lo, hi, swap_out):
            stats["excluded_swap_outage"] = stats.get("excluded_swap_outage", 0) + 1
            continue
        stats["coins"] = stats.get("coins", 0) + 1
        recs = g.astype({c: object for c in g.columns if str(g[c].dtype) == "category"}).to_dict("records")
        for r in recs:
            for k, v in r.items():
                if isinstance(v, float) and v != v:
                    # Missing value -> None. The analysis code tests `t.get("fee_total_bps") is not None` and
                    # `t.get("fee_bps") or 95`; with pandas NaN both silently go wrong (NaN is not None, NaN is
                    # truthy) -> every curve trade's exit fee would be NaN. Bug in the old loader, fixed here.
                    r[k] = None
        yield {"mint": mint, "created": c0, "creator": creator[mint], "trades": recs}


CHUNK_H = 6


def chunk_coins(assets, d, dest, token, stats):
    """Coins created on day d, 6 hours at a time: loads [chunk - 1 h, chunk end + 2 h) (100-min windows complete)."""
    t0 = _hour_ts(d, 0)
    for c in range(0, 24, CHUNK_H):
        born_lo, born_hi = t0 + 3600 * c, t0 + 3600 * (c + CHUNK_H)
        lo, hi = born_lo - 3600, born_hi + 2 * 3600
        need = [a for a in assets if lo <= _hour_ts(a[0], a[1]) < hi]
        if not need:
            continue
        paths = [fetch(a, dest, token) for a in need]
        span_lo = max(lo, START_TS)
        span_hi = min(hi, max(_hour_ts(a[0], a[1]) for a in need) + 3600)
        trades, creates, _ = read_tars(paths)
        yield from coins_from_frames(trades, creates, born_lo, born_hi, span_lo, span_hi, stats)
        del trades, creates


def iter_days(repo=None, token=None, dest=None, end_day=END_DAY, stats=None, only_days=None):
    """Yields (day, generator of coins created that day) in chronological order, downloading as it goes.
    Consume each day's generator before asking for the next day."""
    repo = repo or os.environ.get("GITHUB_REPOSITORY", "wahazzin/memecoin-trader")
    token = token or os.environ.get("GITHUB_TOKEN")
    dest = dest or os.path.join(os.path.dirname(__file__), "out", "raw_day")
    os.makedirs(dest, exist_ok=True)
    first_hour = _hour_ts(date(2026, 10, 7), 20)          # earlier 10-07 files: smoke runs without signatures (A1)
    assets = [a for a in list_assets(repo, token) if _hour_ts(a[0], a[1]) >= first_hour]
    days = all_days(end_day)
    stats = stats if stats is not None else {}
    for i, d in enumerate(days):
        if only_days is not None and d not in only_days:
            continue
        yield d, chunk_coins(assets, d, dest, token, stats)
        keep = {a[2] for a in files_for_day(assets, days[i + 1])} if i + 1 < len(days) else set()
        for p in glob.glob(os.path.join(dest, "*.tar")):
            if os.path.basename(p) not in keep:
                os.remove(p)
    shutil.rmtree(dest, ignore_errors=True)


def all_days(end_day=END_DAY):
    d0 = datetime.fromtimestamp(START_TS, timezone.utc).date()
    return [d0 + timedelta(days=k) for k in range((end_day - d0).days + 1)]


def iter_coins(**kw):
    for _, coins in iter_days(**kw):
        yield from coins
