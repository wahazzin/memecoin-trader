"""Decode pump.fun program events from Solana transaction logs ("Program data: <base64>")."""
import base64
import struct

from memebot import b58

TRADE = bytes.fromhex("bddb7fd34ee661ee")      # sha256("event:TradeEvent")[:8]
COMPLETE = bytes.fromhex("5f72619cd42e9808")   # sha256("event:CompleteEvent")[:8] = bonding curve finished


def trade(raw):
    """TradeEvent: mint, sol, tokens, is_buy, user, ts, vSol, vTok, then (newer versions) realSol, realTok,
    fee_recipient, fee_bps, fee, creator, creator_fee_bps, creator_fee. Returns a list row or None."""
    if len(raw) < 113 or raw[:8] != TRADE:
        return None
    o = 8
    mint = b58.encode(raw[o:o + 32]); o += 32
    sol, tok = struct.unpack_from("<QQ", raw, o); o += 16
    buy = raw[o]; o += 1
    user = b58.encode(raw[o:o + 32]); o += 32
    ts, vsol, vtok = struct.unpack_from("<qQQ", raw, o); o += 24
    if buy not in (0, 1) or not (1.6e9 < ts < 2.2e9):
        return None
    fee = cfee = fee_bps = cfee_bps = None
    creator = None
    if len(raw) >= o + 16 + 32 + 16 + 32 + 16:
        o += 16                                     # real reserves
        o += 32                                     # fee recipient
        fee_bps, fee = struct.unpack_from("<QQ", raw, o); o += 16
        creator = b58.encode(raw[o:o + 32]); o += 32
        cfee_bps, cfee = struct.unpack_from("<QQ", raw, o)
    return {"ts": ts, "mint": mint, "user": user, "buy": bool(buy), "sol": sol / 1e9, "tok": tok / 1e6,
            "vsol": vsol / 1e9, "vtok": vtok / 1e6, "fee": None if fee is None else fee / 1e9,
            "fee_bps": fee_bps, "cfee": None if cfee is None else cfee / 1e9, "cfee_bps": cfee_bps, "creator": creator}


def complete(raw):
    if len(raw) < 8 + 96 or raw[:8] != COMPLETE:
        return None
    return {"user": b58.encode(raw[8:40]), "mint": b58.encode(raw[40:72])}


def events(logs):
    out = []
    for line in logs:
        if not line.startswith("Program data: "):
            continue
        try:
            raw = base64.b64decode(line[14:])
        except Exception:
            continue
        t = trade(raw)
        if t:
            out.append(("trade", t)); continue
        c = complete(raw)
        if c:
            out.append(("complete", c))
    return out
