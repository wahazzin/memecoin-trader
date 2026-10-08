"""rpc.py -- Solana JSON-RPC with fallback. Public RPC first (free, no credits); if it rate-limits or fails,
retry on Helius (secret HELIUS_API_KEY, free plan = 1M credits/month, 1 credit per call). Streams stay on the
public RPC: Helius bills websockets by data volume and our pump.fun stream (~8 GB/day) would use the free
credits up in about a week. The Helius URL contains the key: it is never logged or written to files."""
import os
import time

import requests

PUBLIC = os.environ.get("SOLANA_RPC", "https://api.mainnet-beta.solana.com")
STATS = {"public_ok": 0, "helius_ok": 0, "failed": 0}


def _helius():
    k = os.environ.get("HELIUS_API_KEY")
    return f"https://mainnet.helius-rpc.com/?api-key={k}" if k else None


def call(method, params, timeout=20):
    body = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    for attempt, url in enumerate([PUBLIC, PUBLIC, _helius()]):
        if not url:
            continue
        try:
            r = requests.post(url, json=body, timeout=timeout)
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(0.5 * (attempt + 1)); continue
            js = r.json()
            if "error" in js and js["error"].get("code") in (-32005, -32429, 429):   # rate limited
                continue
            STATS["helius_ok" if url != PUBLIC else "public_ok"] += 1
            return js.get("result")
        except Exception:
            time.sleep(0.3)
    STATS["failed"] += 1
    return None
