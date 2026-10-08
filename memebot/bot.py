"""
bot.py -- live PAPER trading bot for fresh pump.fun coins. Read-only on the blockchain; all fills via
memebot.paper (live Jupiter quotes). No wallet, no keys, cannot trade real money.

Arms (forward paper test, rules fixed in research/M1_PREREG.md + BOT_SPEC.md):
  m1_pass    buy at the M1 checkpoint if ALL Setuh checks pass
  m1_random  CONTROL: buy at the M1 checkpoint for a random 10% of ALL checkpoint coins (checks ignored)
Exit for both: +50% / -20% price, 15 min without trades, 60 min max (same as M1's mechanical trade).

State lives in --state (a git branch in CI): positions.json, orders.jsonl, equity.jsonl, events.jsonl.
"""
import argparse
import asyncio
import json
import os
import random
import time
from collections import defaultdict

from memebot import paper
from memebot.decode import events as decode_events
from research.m1 import coin_checks          # the SAME check code as the pre-registered M1 test

PUMP = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
AMM = "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"
RPC_WS = os.environ.get("SOLANA_WS", "wss://api.mainnet-beta.solana.com")
ARMS = {"m1_pass": {"bankroll": 20.0}, "m1_random": {"bankroll": 20.0}}
SIZE = 0.5
MAX_OPEN = 10
DAILY_LOSS_LIMIT = 0.15        # circuit breaker: an arm that loses 15% of its day-start equity stops for the day
CONTROL_RATE = 0.10


def curve_address(mint):
    """The coin's bonding-curve account, derived from its mint (seeds "bonding-curve" + mint, pump.fun program).
    Not taken from any feed: a feed once reported a wallet here."""
    from solders.pubkey import Pubkey
    try:
        return str(Pubkey.find_program_address([b"bonding-curve", bytes(Pubkey.from_string(mint))],
                                               Pubkey.from_string(PUMP))[0])
    except Exception:
        return None


def read_curve(key, rpc=os.environ.get("SOLANA_RPC", "https://api.mainnet-beta.solana.com")):
    import base64
    import struct
    import requests
    if not key:
        return None
    try:
        r = requests.post(rpc, json={"jsonrpc": "2.0", "id": 1, "method": "getAccountInfo",
                                     "params": [key, {"encoding": "base64", "commitment": "confirmed"}]}, timeout=15).json()
        if r["result"]["value"]["owner"] != PUMP:
            return None                                   # not a pump.fun curve account
        raw = base64.b64decode(r["result"]["value"]["data"][0])
        vtok, vsol = struct.unpack_from("<QQ", raw, 8)
        return {"vtok": vtok / 1e6, "vsol": vsol / 1e9, "complete": bool(raw[48])}
    except Exception:
        return None


class State:
    def __init__(self, d):
        self.d = d
        os.makedirs(d, exist_ok=True)
        self.pos = self._load("positions.json", {a: {} for a in ARMS})
        self.cash = self._load("cash.json", {a: v["bankroll"] for a, v in ARMS.items()})
        self.day = self._load("day.json", {})
        self.known_accounts = self._load("accounts.json", {a: [] for a in ARMS})

    def _load(self, name, default):
        p = os.path.join(self.d, name)
        return json.load(open(p)) if os.path.exists(p) else default

    def save(self):
        for name, obj in (("positions.json", self.pos), ("cash.json", self.cash), ("day.json", self.day),
                          ("accounts.json", self.known_accounts)):
            with open(os.path.join(self.d, name), "w") as f:
                json.dump(obj, f, indent=1)

    def log(self, name, rec):
        with open(os.path.join(self.d, name), "a") as f:
            f.write(json.dumps(rec, default=str) + "\n")


class Bot:
    def __init__(self, state, dry_quotes=None):
        self.s = state
        self.coins = {}                 # mint -> {created, creator, trades: [...], done}
        self.price = {}                 # mint -> last price (SOL per token, from on-chain events)
        self.last_trade = {}            # mint -> ts
        self.curve = {}                 # mint -> (vsol, vtok, fee_frac) from the latest on-chain trade event
        self.busy = set()
        self.pools = {}                 # PumpSwap pool -> mint, for coins we hold that graduated
        self.rng = random.Random()

    # ---------- market data ----------
    def on_create(self, m):
        self.coins[m["mint"]] = {"created": time.time(), "creator": m.get("traderPublicKey"), "trades": [], "done": False,
                                 "curve_key": curve_address(m["mint"])}

    def on_trade(self, t):
        from memebot.decode import is_sol_coin
        mint = t["mint"]
        if not is_sol_coin(t):
            c = self.coins.get(mint)
            if c:
                c["done"] = True; c["trades"] = []          # not priced in SOL: never traded by this bot
            return None
        price = t["vsol"] / t["vtok"] if t["vtok"] and t["vsol"] else None
        if price:
            self.price[mint] = price
            self.last_trade[mint] = t["ts"]
            fee = (t["fee_total_bps"] if t.get("fee_total_bps") is not None
                   else (t.get("fee_bps") or 95) + (t.get("cfee_bps") or 30)) / 1e4
            self.curve[mint] = (t["vsol"], t["vtok"], fee)
        c = self.coins.get(mint)
        if c is None or c["done"] or price is None:
            return None
        t = {**t, "price": price}
        c["trades"].append(t)
        launch = c["trades"][0]["price"]
        age = t["ts"] - c["created"]
        if age > 2400:
            c["done"] = True; c["trades"] = []
            return None
        if price >= 2.5 * launch:                      # M1 checkpoint
            c["done"] = True
            chk = coin_checks(c["trades"], c["creator"])
            hold = defaultdict(float)
            for x in c["trades"]:
                hold[x["user"]] += x["tok"] if x["buy"] else -x["tok"]
            top10 = [u for u, v in sorted(hold.items(), key=lambda kv: -kv[1])[:10] if v > 0]
            fee_bps = max((x.get("cfee_bps") or 0) for x in c["trades"])
            sig = {"mint": mint, "ts": t["ts"], "age_s": round(age), "checks": chk, "pass": all(chk.values()),
                   "creator_fee_bps": fee_bps, "price": price, "curve_key": c.get("curve_key"),
                   "fee_frac": ((t.get("fee_bps") or 95) + (t.get("cfee_bps") or 30)) / 1e4, "top10": top10}
            c["trades"] = []
            return sig
        return None

    # ---------- trading ----------
    def day_ok(self, arm):
        today = time.strftime("%Y-%m-%d", time.gmtime())
        d = self.s.day.setdefault(arm, {})
        if d.get("date") != today:
            d.update(date=today, start=self.equity(arm), halted=False)
        if not d["halted"] and self.equity(arm) < d["start"] * (1 - DAILY_LOSS_LIMIT):
            d["halted"] = True
            self.s.log("events.jsonl", {"ts": time.time(), "type": "CIRCUIT_BREAKER", "arm": arm,
                                        "equity": self.equity(arm), "day_start": d["start"]})
            from memebot import notify
            notify.send(f"🛑 Memecoin paper bot: circuit breaker on `{arm}` (lost >{DAILY_LOSS_LIMIT:.0%} today, "
                        f"equity {self.equity(arm):.2f} SOL). It stops buying until 00:00 UTC. Paper only.")
        return not d["halted"]

    def equity(self, arm):
        """Cash + what the open positions would actually return if sold now (curve formula incl. fees and
        price impact, minus the sell's fixed costs), not tokens x last price."""
        from memebot.curve import sell_sol
        val = 0.0
        for mint, p in self.s.pos[arm].items():
            c = self.curve.get(mint)
            if c:
                val += max(sell_sol(c[0], c[1], p["tokens"], c[2]) - paper.PRIORITY_SOL - paper.NETWORK_SOL, 0)
            else:
                val += p.get("last_value", p["cost"])     # no stream data since restart: last known sell value
        return self.s.cash[arm] + val

    async def enter(self, arm, sig):
        if len(self.s.pos[arm]) >= MAX_OPEN or self.s.cash[arm] < SIZE + 0.01 or not self.day_ok(arm):
            self.s.log("events.jsonl", {"ts": time.time(), "type": "SKIP", "arm": arm, "mint": sig["mint"],
                                        "why": "max_open/cash/circuit_breaker"})
            return
        first = sig["mint"] not in self.s.known_accounts[arm]
        rec = await asyncio.to_thread(paper.buy, sig["mint"], SIZE, first)
        rec.update(arm=arm, signal=sig)
        self.s.log("orders.jsonl", rec)
        if rec["status"] == "FILLED":
            self.s.cash[arm] -= rec["cost_sol"]
            entry_price = (SIZE / 1.0125) / rec["tokens"] if rec["tokens"] else sig["price"]   # SOL/token paid
            self.s.pos[arm][sig["mint"]] = {"tokens": rec["tokens"], "cost": rec["cost_sol"], "opened": time.time(),
                                            "entry_price": self.price.get(sig["mint"], sig["price"]),
                                            "paid_price": entry_price, "curve_key": sig.get("curve_key"),
                                            "fee_frac": sig.get("fee_frac", 0.0125)}
            self.s.known_accounts[arm].append(sig["mint"])
        elif rec["status"] == "FAILED":
            self.s.cash[arm] -= rec["cost_sol"]
        self.s.save()

    def exit_reason(self, p, mint, now):
        pr = self.price.get(mint)
        if pr is not None and pr >= 1.5 * p["entry_price"]:
            return "take_profit"
        if pr is not None and pr <= 0.8 * p["entry_price"]:
            return "stop_loss"
        if now - self.last_trade.get(mint, p["opened"]) > 900:
            return "no_volume_15m"
        if now - p["opened"] > 3600:
            return "max_hold_60m"
        return None

    async def exit(self, arm, mint, why):
        p = self.s.pos[arm][mint]
        def curve_now():
            """Live reserves straight from the coin's bonding-curve account on the blockchain (same input Jupiter
            uses). None if the curve is complete (coin graduated -> only Jupiter/PumpSwap can price it)."""
            c = read_curve(p.get("curve_key"))
            if c and not c["complete"]:
                return (c["vsol"], c["vtok"], p.get("fee_frac", 0.0125), 0)
            return None
        rec = await asyncio.to_thread(paper.sell, mint, p["tokens"], True, time.sleep, curve_now)
        rec.update(arm=arm, why=why)
        if rec["status"] == "FILLED":
            pnl = rec["proceeds_sol"] - p["cost"]
            rec.update(pnl_sol=pnl, ret=pnl / p["cost"], held_s=round(time.time() - p["opened"]))
            self.s.cash[arm] += rec["proceeds_sol"]
            del self.s.pos[arm][mint]
            self.s.known_accounts[arm].remove(mint)
        elif rec["status"] == "FAILED":
            self.s.cash[arm] += rec["proceeds_sol"]          # fees lost, position kept, retried next loop
        else:
            p["stuck_since"] = p.get("stuck_since") or time.time()   # no route: keep trying, stays marked
            p["last_try"] = time.time()
        self.s.log("orders.jsonl", rec)
        self.s.save()

    async def manage(self, stop):
        while time.time() < stop:
            await asyncio.sleep(3)
            now = time.time()
            for arm in ARMS:
                for mint, p in list(self.s.pos[arm].items()):
                    if (arm, mint) in self.busy:
                        continue
                    if p.get("stuck_since") and now - p.get("last_try", 0) < 60:
                        continue                                  # no sell route: retry once a minute
                    why = self.exit_reason(p, mint, now)
                    if why:
                        self.busy.add((arm, mint))
                        try:
                            await self.exit(arm, mint, why)
                        finally:
                            self.busy.discard((arm, mint))

    async def record_funding(self, sig):
        """M1b data: who funded the top holders. Recorded only; not used for trading until M1b is tested."""
        from memebot import funding
        try:
            ws = [await asyncio.to_thread(funding.wallet, w) for w in sig.get("top10", [])]
            self.s.log("funding.jsonl", {"mint": sig["mint"], "ts": sig["ts"], **funding.summarize(ws)})
        except Exception as e:
            self.s.log("events.jsonl", {"ts": time.time(), "type": "FUNDING_ERROR", "error": type(e).__name__})

    async def handle_signal(self, sig):
        self.s.log("signals.jsonl", sig)
        asyncio.create_task(self.record_funding(sig))
        arms = []
        if sig["pass"]:
            arms.append("m1_pass")
        if self.rng.random() < CONTROL_RATE:
            arms.append("m1_random")
        for a in arms:
            await self.enter(a, sig)

    async def snapshot(self, stop):
        while time.time() < stop:
            await asyncio.sleep(300)
            cutoff = time.time() - 3 * 3600
            self.coins = {m: c for m, c in self.coins.items() if c["created"] > cutoff}
            for arm in ARMS:
                self.s.log("equity.jsonl", {"ts": time.time(), "arm": arm, "equity": self.equity(arm),
                                            "cash": self.s.cash[arm], "open": len(self.s.pos[arm])})
            self.s.save()


async def stream(bot, stop):
    import websockets
    async def rpc(program=PUMP):
        while time.time() < stop:
            try:
                async with websockets.connect(RPC_WS, max_size=2 ** 24, ping_interval=20, ping_timeout=60) as ws:
                    await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                              "params": [{"mentions": [program]}, {"commitment": "confirmed"}]}))
                    while time.time() < stop:
                        m = json.loads(await asyncio.wait_for(ws.recv(), timeout=60))
                        v = (m.get("params", {}).get("result", {}) or {}).get("value") or {}
                        if not v or v.get("err"):
                            continue
                        for kind, d in decode_events(v.get("logs", [])):
                            if kind == "trade":
                                sig = bot.on_trade(d)
                                if sig:
                                    asyncio.create_task(bot.handle_signal(sig))
                            elif kind == "migrated":
                                bot.pools[d["pool"]] = d["mint"]
                            elif kind == "amm_trade" and d["pool"] in bot.pools:
                                from memebot.decode import amm_row
                                r = amm_row(d, bot.pools[d["pool"]])
                                if r:
                                    bot.on_trade(r)
            except Exception as e:
                bot.s.log("events.jsonl", {"ts": time.time(), "type": "GAP", "source": "rpc", "error": f"{type(e).__name__}"})
                await asyncio.sleep(2)
    async def pp():
        while time.time() < stop:
            try:
                async with websockets.connect("wss://pumpportal.fun/api/data", ping_interval=20) as ws:
                    await ws.send(json.dumps({"method": "subscribeNewToken"}))
                    while time.time() < stop:
                        m = json.loads(await asyncio.wait_for(ws.recv(), timeout=120))
                        if m.get("txType") == "create":
                            bot.on_create(m)
            except Exception as e:
                bot.s.log("events.jsonl", {"ts": time.time(), "type": "GAP", "source": "pumpportal", "error": f"{type(e).__name__}"})
                await asyncio.sleep(3)
    await asyncio.gather(rpc(), rpc(AMM), pp(), bot.manage(stop), bot.snapshot(stop))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", default="paper_state")
    ap.add_argument("--minutes", type=float, default=330)
    a = ap.parse_args()
    s = State(a.state)
    s.log("events.jsonl", {"ts": time.time(), "type": "START", "open": {k: len(v) for k, v in s.pos.items()}})
    asyncio.run(stream(Bot(s), time.time() + a.minutes * 60))
    s.save()
    s.log("events.jsonl", {"ts": time.time(), "type": "STOP"})


if __name__ == "__main__":
    main()
