"""probe_create.py -- check the on-chain CreateEvent decoder against PumpPortal for N seconds (added 2026-11-23).
Prints how many new coins each source saw, how many match, and whether name/symbol/creator agree."""
import asyncio
import json
import os
import sys
import time

from memebot.decode import events as decode_events
from memebot.recorder import PUMP, RPC_WS

SECS = float(sys.argv[1]) if len(sys.argv) > 1 else 120


async def main():
    import websockets
    chain, pp, stop = {}, {}, time.time() + SECS

    async def rpc():
        async with websockets.connect(RPC_WS, max_size=2 ** 24, ping_interval=20) as ws:
            await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                      "params": [{"mentions": [PUMP]}, {"commitment": "confirmed"}]}))
            while time.time() < stop:
                try:
                    m = json.loads(await asyncio.wait_for(ws.recv(), timeout=5))
                except asyncio.TimeoutError:
                    continue
                v = (m.get("params", {}).get("result", {}) or {}).get("value") or {}
                for kind, d in decode_events(v.get("logs", []) if v else []):
                    if kind == "create":
                        chain[d["mint"]] = d

    async def portal():
        async with websockets.connect("wss://pumpportal.fun/api/data", ping_interval=20) as ws:
            await ws.send(json.dumps({"method": "subscribeNewToken"}))
            while time.time() < stop:
                try:
                    m = json.loads(await asyncio.wait_for(ws.recv(), timeout=5))
                except asyncio.TimeoutError:
                    continue
                if m.get("txType") == "create":
                    pp[m["mint"]] = m

    await asyncio.gather(rpc(), portal(), return_exceptions=True)
    both = set(chain) & set(pp)
    agree = sum(chain[m]["user"] == pp[m].get("traderPublicKey") and chain[m]["symbol"] == pp[m].get("symbol")
                for m in both)
    out = [f"# CreateEvent decoder check ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}, {SECS:.0f} s)", "",
           f"- on-chain creates decoded: {len(chain)}", f"- PumpPortal creates: {len(pp)}",
           f"- in both: {len(both)}; creator + symbol agree: {agree}",
           f"- chain only: {len(set(chain) - set(pp))}; PumpPortal only: {len(set(pp) - set(chain))}"]
    if both:
        m = sorted(both)[0]
        out.append(f"- example: chain {json.dumps({k: chain[m][k] for k in ('mint', 'symbol', 'user', 'vsol', 'vtok')})}")
    text = "\n".join(out)
    print(text)
    os.makedirs("research/out", exist_ok=True)
    open("research/out/probe_create.md", "w").write(text + "\n")


if __name__ == "__main__":
    asyncio.run(main())
