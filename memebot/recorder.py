"""
recorder.py -- records the pump.fun market 24/7, read-only (no wallet, no keys).

Sources:  Solana public RPC logsSubscribe on the pump.fun program -> every trade + curve completions
          PumpPortal websocket -> every new coin (name, symbol, creator, dev buy) + migrations
Output (one folder per UTC hour, parquet, zstd):
  creates.parquet   every new coin
  trades.parquet    EVERY trade of coins up to 60 min old (tick data: scam checks, dip entries, exits)
  candles.parquet   1-minute candles for EVERY coin, any age (price in SOL, volume, buyers/sellers)
  events.parquet    curve completions / migrations
  status.json       uptime, reconnects, counts (gaps are logged, never hidden)
Usage: python -m memebot.recorder --minutes 340 --out data
"""
import argparse
import asyncio
import hashlib
import json
import os
import time
from collections import defaultdict

from memebot.decode import events as decode_events

PUMP = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
RPC_WS = os.environ.get("SOLANA_WS", "wss://api.mainnet-beta.solana.com")
TICK_MAX_AGE = 3600          # keep every trade for a coin's first 60 minutes


class Store:
    def __init__(self, out):
        self.out = out
        self.hour = None
        self.reset()
        self.created = {}        # mint -> create ts (coins born while we listen)
        self.first_seen = {}     # mint -> first trade ts (coins born before we started)
        self.seen_sigs = set()
        self.stats = defaultdict(int)
        self.gaps = []

    def reset(self):
        self.creates, self.trades, self.events = [], [], []
        self.candles = {}        # (mint, minute) -> [o,h,l,c, buy_sol, sell_sol, n_buys, n_sells, users(set)]

    def age(self, mint, ts):
        born = self.created.get(mint)
        if born is None:
            return None
        return ts - born

    def add_trade(self, t, slot, sig):
        key = hashlib.blake2b(sig.encode(), digest_size=8).hexdigest() + str(t["mint"][:6]) + str(t["sol"])
        if key in self.seen_sigs:
            self.stats["dup"] += 1
            return
        self.seen_sigs.add(key)
        self.roll(t["ts"])
        self.first_seen.setdefault(t["mint"], t["ts"])
        price = t["vsol"] / t["vtok"] if t["vtok"] else None
        age = self.age(t["mint"], t["ts"])
        if age is not None and age <= TICK_MAX_AGE:
            self.trades.append({**t, "slot": slot, "sig": sig, "price": price})   # full sig = audit trail
            self.stats["ticks"] += 1
        if price:
            k = (t["mint"], t["ts"] // 60 * 60)
            c = self.candles.get(k)
            if c is None:
                c = self.candles[k] = [price, price, price, price, 0.0, 0.0, 0, 0, set()]
            c[1], c[2], c[3] = max(c[1], price), min(c[2], price), price
            c[4 if t["buy"] else 5] += t["sol"]
            c[6 if t["buy"] else 7] += 1
            c[8].add(t["user"])
        self.stats["trades"] += 1

    def add_create(self, m):
        ts = int(time.time())
        self.roll(ts)
        self.created.setdefault(m["mint"], ts)
        self.creates.append({"ts": ts, "mint": m.get("mint"), "name": m.get("name"), "symbol": m.get("symbol"),
                             "uri": m.get("uri"), "creator": m.get("traderPublicKey"),
                             "dev_buy_sol": m.get("solAmount"), "dev_buy_tok": m.get("initialBuy"),
                             "vsol": m.get("vSolInBondingCurve"), "vtok": m.get("vTokensInBondingCurve"),
                             "mcap_sol": m.get("marketCapSol"), "pool": m.get("pool"),
                             "mayhem": m.get("is_mayhem_mode"), "sig": m.get("signature") or ""})
        self.stats["creates"] += 1

    def add_event(self, kind, d, ts=None):
        ts = ts or int(time.time())
        self.roll(ts)
        self.events.append({"ts": ts, "kind": kind, "mint": d.get("mint"), "detail": json.dumps(d)[:400]})
        self.stats[kind] += 1

    def roll(self, ts):
        h = time.strftime("%Y-%m-%d/%H", time.gmtime(ts))
        if self.hour is None:
            self.hour = h
        elif h > self.hour and ts > time.time() - 120:      # forward only; late trades go in the open file
            self.flush()
            self.hour = h

    def flush(self, final=False):
        import pyarrow as pa
        import pyarrow.parquet as pq
        if self.hour is None:
            return
        d = os.path.join(self.out, self.hour)
        os.makedirs(d, exist_ok=True)
        self.nflush = getattr(self, "nflush", 0) + 1       # unique per process: never overwrite a file
        part = f"{os.environ.get('GITHUB_RUN_ID', 'local')}_{self.nflush:04d}_{time.strftime('%M%S')}"
        def write(name, rows):
            if rows:
                pq.write_table(pa.Table.from_pylist(rows), os.path.join(d, f"{name}_{part}.parquet"),
                               compression="zstd")
        write("creates", self.creates)
        write("trades", self.trades)
        write("events", self.events)
        write("candles", [{"mint": m, "t": t, "o": c[0], "h": c[1], "l": c[2], "c": c[3], "buy_sol": c[4],
                           "sell_sol": c[5], "n_buys": c[6], "n_sells": c[7], "n_users": len(c[8])}
                          for (m, t), c in self.candles.items()])
        with open(os.path.join(d, f"status_{part}.json"), "w") as f:
            json.dump({"hour": self.hour, "written_at": int(time.time()), "final": final, "stats": dict(self.stats),
                       "gaps": self.gaps, "rows": {"creates": len(self.creates), "trades": len(self.trades),
                                                   "candles": len(self.candles), "events": len(self.events)}}, f)
        print(f"[flush] {self.hour}: {len(self.creates)} creates, {len(self.trades)} ticks, "
              f"{len(self.candles)} candles", flush=True)
        self.reset()
        # forget coins older than 6h to bound memory
        cutoff = time.time() - 6 * 3600
        self.created = {k: v for k, v in self.created.items() if v > cutoff}
        self.first_seen = {k: v for k, v in self.first_seen.items() if v > cutoff}
        if len(self.seen_sigs) > 2_000_000:
            self.seen_sigs = set()


async def rpc_stream(store, stop):
    import websockets
    while time.time() < stop:
        t_down = None
        try:
            async with websockets.connect(RPC_WS, max_size=2 ** 24, ping_interval=20, ping_timeout=60) as ws:
                await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                          "params": [{"mentions": [PUMP]}, {"commitment": "confirmed"}]}))
                store.stats["rpc_connects"] += 1
                while time.time() < stop:
                    m = json.loads(await asyncio.wait_for(ws.recv(), timeout=60))
                    r = m.get("params", {}).get("result", {})
                    v, slot = r.get("value") or {}, (r.get("context") or {}).get("slot")
                    if not v or v.get("err"):
                        continue
                    for kind, d in decode_events(v.get("logs", [])):
                        if kind == "trade":
                            store.add_trade(d, slot, v.get("signature", ""))
                        else:
                            store.add_event("curve_complete", d)
        except Exception as e:
            t_down = int(time.time())
            store.stats["rpc_errors"] += 1
            store.gaps.append({"source": "rpc", "at": t_down, "error": f"{type(e).__name__}: {str(e)[:120]}"})
            print("rpc reconnect:", type(e).__name__, str(e)[:120], flush=True)
            await asyncio.sleep(2)


async def pumpportal_stream(store, stop):
    import websockets
    while time.time() < stop:
        try:
            async with websockets.connect("wss://pumpportal.fun/api/data", max_size=2 ** 22, ping_interval=20) as ws:
                await ws.send(json.dumps({"method": "subscribeNewToken"}))
                await ws.send(json.dumps({"method": "subscribeMigration"}))
                store.stats["pp_connects"] += 1
                while time.time() < stop:
                    m = json.loads(await asyncio.wait_for(ws.recv(), timeout=120))
                    if m.get("txType") == "create":
                        store.add_create(m)
                    elif "mint" in m and "message" not in m:
                        store.add_event("migration", m)
        except Exception as e:
            store.stats["pp_errors"] += 1
            store.gaps.append({"source": "pumpportal", "at": int(time.time()), "error": f"{type(e).__name__}: {str(e)[:120]}"})
            await asyncio.sleep(3)


async def main_async(minutes, out):
    store = Store(out)
    stop = time.time() + minutes * 60
    async def ticker():
        while time.time() < stop:
            await asyncio.sleep(30)
            store.roll(int(time.time()))
    await asyncio.gather(rpc_stream(store, stop), pumpportal_stream(store, stop), ticker())
    store.flush(final=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=340)
    ap.add_argument("--out", default="data")
    a = ap.parse_args()
    asyncio.run(main_async(a.minutes, a.out))


if __name__ == "__main__":
    main()
