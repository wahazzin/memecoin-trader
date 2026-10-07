"""
probe.py -- READ-ONLY feasibility probe: which free memecoin data sources work, what they contain,
and how much data there is. No trading, no wallet, no keys. Output: research/out/probe/probe.md + samples.

Sources checked:
  1. PumpPortal websocket (live): new tokens, trades on those tokens, migrations
  2. Solana public RPC: can we read a wallet's history (needed for "who funded the top holders")
  3. DexScreener + GeckoTerminal: migrated-pool data and OHLCV
  4. pump.fun public frontend API: coin details
"""
import asyncio
import json
import os
import time
from collections import Counter

import requests

OUT = os.path.join(os.path.dirname(__file__), "out", "probe")
LINES = []


def log(s=""):
    print(s, flush=True)
    LINES.append(s)


def save(name, obj):
    with open(os.path.join(OUT, name), "w") as f:
        json.dump(obj, f, indent=1, default=str)


async def pumpportal(seconds=240, follow=40):
    import websockets
    new, trades, migr, errs = [], [], [], []
    followed = []
    t0 = time.time()
    try:
        async with websockets.connect("wss://pumpportal.fun/api/data", max_size=2 ** 22) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            await ws.send(json.dumps({"method": "subscribeMigration"}))
            while time.time() - t0 < seconds:
                try:
                    msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=30))
                except asyncio.TimeoutError:
                    continue
                kind = msg.get("txType")
                if kind == "create":
                    new.append(msg)
                    if len(followed) < follow:
                        followed.append(msg["mint"])
                        await ws.send(json.dumps({"method": "subscribeTokenTrade", "keys": [msg["mint"]]}))
                elif kind in ("buy", "sell"):
                    trades.append(msg)
                elif kind == "migrate" or "migrat" in json.dumps(msg)[:200].lower():
                    migr.append(msg)
                else:
                    errs.append(msg)
    except Exception as e:
        log(f"- PumpPortal ERROR: {type(e).__name__}: {e}")
    mins = (time.time() - t0) / 60
    log(f"## 1. PumpPortal websocket ({mins:.1f} min)")
    log(f"- new tokens: {len(new)} (~{len(new) / mins * 60 * 24:,.0f}/day)")
    log(f"- trades on the first {len(followed)} new tokens: {len(trades)}; per token: "
        f"{Counter(t['mint'] for t in trades).most_common(5)}")
    log(f"- migrations: {len(migr)}; other messages: {len(errs)}")
    if new:
        log(f"- create fields: {sorted(new[0].keys())}")
    if trades:
        log(f"- trade fields: {sorted(trades[0].keys())}")
        pools = Counter(t.get("pool") for t in trades)
        log(f"- trade pools: {dict(pools)}")
    save("pp_new.json", new[:20]); save("pp_trades.json", trades[:200]); save("pp_migr.json", migr[:10]); save("pp_other.json", errs[:10])
    return new, trades


def rpc(method, params):
    r = requests.post("https://api.mainnet-beta.solana.com", json={"jsonrpc": "2.0", "id": 1, "method": method,
                                                                    "params": params}, timeout=30)
    return r.status_code, r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text[:200]


def solana_rpc(trades):
    log("\n## 2. Solana public RPC (wallet history = funding-source checks)")
    if not trades:
        log("- skipped: no trades captured"); return
    wallet = trades[0].get("traderPublicKey")
    sc, js = rpc("getSignaturesForAddress", [wallet, {"limit": 20}])
    log(f"- getSignaturesForAddress(trader): HTTP {sc}, {len(js.get('result', [])) if isinstance(js, dict) else js}")
    if isinstance(js, dict) and js.get("result"):
        oldest = js["result"][-1]["signature"]
        sc2, tx = rpc("getTransaction", [oldest, {"maxSupportedTransactionVersion": 0, "encoding": "jsonParsed"}])
        ok = isinstance(tx, dict) and tx.get("result")
        log(f"- getTransaction(oldest of those): HTTP {sc2}, {'ok' if ok else tx}")
        save("rpc_tx.json", tx)
    mint = trades[0]["mint"]
    sc3, js3 = rpc("getTokenLargestAccounts", [mint])
    log(f"- getTokenLargestAccounts(mint): HTTP {sc3}, {len(js3.get('result', {}).get('value', [])) if isinstance(js3, dict) and 'result' in js3 else js3}")
    hits = 0
    t = time.time()
    for _ in range(30):
        s, _j = rpc("getSlot", [])
        hits += s == 200
    log(f"- rate test: {hits}/30 getSlot OK in {time.time() - t:.1f}s")


def http_get(url):
    try:
        r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        return r.status_code, (r.json() if "json" in r.headers.get("content-type", "") else r.text[:300])
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def dex_sources(new):
    log("\n## 3. DexScreener / GeckoTerminal")
    sc, js = http_get("https://api.geckoterminal.com/api/v2/networks/solana/dexes/pumpswap/pools?page=1")
    pools = js.get("data", []) if isinstance(js, dict) else []
    log(f"- GeckoTerminal PumpSwap pools: HTTP {sc}, {len(pools)} pools")
    if pools:
        addr = pools[0]["attributes"]["address"]
        sc2, oh = http_get(f"https://api.geckoterminal.com/api/v2/networks/solana/pools/{addr}/ohlcv/minute?aggregate=1&limit=1000")
        n = len(oh.get("data", {}).get("attributes", {}).get("ohlcv_list", [])) if isinstance(oh, dict) else oh
        log(f"- GeckoTerminal 1-min OHLCV for one migrated pool: HTTP {sc2}, {n} candles")
    if new:
        sc3, ds = http_get(f"https://api.dexscreener.com/tokens/v1/solana/{new[0]['mint']}")
        log(f"- DexScreener token (brand-new pump coin): HTTP {sc3}, {str(ds)[:150]}")
    sc4, ds4 = http_get("https://api.dexscreener.com/token-profiles/latest/v1")
    log(f"- DexScreener latest paid profiles: HTTP {sc4}, {len(ds4) if isinstance(ds4, list) else str(ds4)[:120]}")


def pumpfun_api(new):
    log("\n## 4. pump.fun public frontend API")
    if not new:
        log("- skipped"); return
    for base in ("https://frontend-api-v3.pump.fun", "https://frontend-api.pump.fun"):
        sc, js = http_get(f"{base}/coins/{new[0]['mint']}")
        log(f"- {base}/coins/<mint>: HTTP {sc}, keys {sorted(js.keys())[:25] if isinstance(js, dict) else str(js)[:120]}")
        if isinstance(js, dict):
            save("pf_coin.json", js)
            break


def main():
    os.makedirs(OUT, exist_ok=True)
    log(f"# Data probe {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}\n")
    new, trades = asyncio.run(pumpportal())
    solana_rpc(trades)
    dex_sources(new)
    pumpfun_api(new)
    with open(os.path.join(OUT, "probe.md"), "w") as f:
        f.write("\n".join(LINES) + "\n")


if __name__ == "__main__":
    main()
