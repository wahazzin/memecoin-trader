"""
funding.py -- who funded a coin's top holders, read from the blockchain (read-only).
For each wallet: how many transactions it has ever made (capped), how old it is, and -- for fresh wallets --
which wallet sent it its first SOL and when. Bundles show up as several fresh wallets funded by the same
source within minutes (Setuh: "funded from the exact same place at the exact same time").
"""
import os
import time

import requests

RPC = os.environ.get("SOLANA_RPC", "https://api.mainnet-beta.solana.com")
FRESH_TX = 50          # a wallet with fewer than 50 transactions ever = "fresh"


def rpc(method, params):
    from memebot.rpc import call
    return call(method, params)                          # public RPC, Helius fallback


def wallet(addr):
    sigs = rpc("getSignaturesForAddress", [addr, {"limit": FRESH_TX}])
    if sigs is None:
        return {"wallet": addr, "error": "rpc"}
    out = {"wallet": addr, "n_tx": len(sigs), "fresh": len(sigs) < FRESH_TX}
    if not sigs:
        return out
    oldest = sigs[-1]
    out["first_seen"] = oldest.get("blockTime")
    if out["fresh"]:                                   # we have its whole history: find who funded it
        tx = rpc("getTransaction", [oldest["signature"], {"maxSupportedTransactionVersion": 0, "encoding": "jsonParsed"}])
        try:
            ixs = list(tx["transaction"]["message"]["instructions"])
            for inner in tx["meta"].get("innerInstructions") or []:
                ixs += inner["instructions"]
            for ix in ixs:
                p = ix.get("parsed") if isinstance(ix, dict) else None
                if isinstance(p, dict) and p.get("type") == "transfer" and p["info"].get("destination") == addr:
                    out["funder"] = p["info"]["source"]
                    out["funded_sol"] = p["info"].get("lamports", 0) / 1e9
                    out["funded_at"] = tx.get("blockTime")
                    break
        except Exception:
            out["funder_error"] = True
    return out


def summarize(wallets):
    """Bundle features from a list of wallet() results (top holders)."""
    ok = [w for w in wallets if "error" not in w]
    fresh = [w for w in ok if w.get("fresh")]
    by_funder = {}
    for w in fresh:
        if w.get("funder"):
            by_funder.setdefault(w["funder"], []).append(w)
    biggest = max(by_funder.values(), key=len) if by_funder else []
    times = sorted(w["funded_at"] for w in biggest if w.get("funded_at"))
    return {"n_checked": len(ok), "n_fresh": len(fresh), "max_same_funder": len(biggest),
            "same_funder_window_s": (times[-1] - times[0]) if len(times) >= 2 else None,
            "wallets": ok}
