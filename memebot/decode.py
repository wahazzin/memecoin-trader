"""Decode pump.fun program events from Solana transaction logs ("Program data: <base64>")."""
import base64
import struct

from memebot import b58

TRADE = bytes.fromhex("bddb7fd34ee661ee")      # sha256("event:TradeEvent")[:8]
COMPLETE = bytes.fromhex("5f72619cd42e9808")   # sha256("event:CompleteEvent")[:8] = bonding curve finished
MIGRATED = bytes(b for b in [189, 233, 93, 185, 92, 148, 234, 148])     # CompletePumpAmmMigrationEvent (mint -> pool)
POSTBUY = bytes([111, 176, 109, 139, 49, 108, 213, 251])                # PostCompleteBuyEvent (synthetic migration)
AMM_BUY = bytes([103, 244, 82, 31, 44, 245, 119, 119])
AMM_SELL = bytes([62, 47, 55, 10, 165, 3, 220, 42])
AMM_CREATE = bytes([177, 49, 12, 210, 160, 118, 167, 116])
SOL_MINTS = {"So11111111111111111111111111111111111111112", "11111111111111111111111111111111"}
# Layouts: pump.fun official IDLs (github.com/pump-fun/pump-public-docs, idl/pump.json + pump_amm.json)


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
    ext = {}
    if len(raw) >= o + 16 + 32 + 16 + 32 + 16:
        o += 16                                     # real reserves
        o += 32                                     # fee recipient
        fee_bps, fee = struct.unpack_from("<QQ", raw, o); o += 16
        creator = b58.encode(raw[o:o + 32]); o += 32
        cfee_bps, cfee = struct.unpack_from("<QQ", raw, o); o += 16
        ext = _trade_tail(raw, o)
    return {"ts": ts, "mint": mint, "user": user, "buy": bool(buy), "sol": sol / 1e9, "tok": tok / 1e6,
            "vsol": vsol / 1e9, "vtok": vtok / 1e6, "fee": None if fee is None else fee / 1e9,
            "fee_bps": fee_bps, "cfee": None if cfee is None else cfee / 1e9, "cfee_bps": cfee_bps, "creator": creator, **ext}


def _trade_tail(raw, o):
    """Fields after creator_fee (newer TradeEvent versions). Missing trailing fields = absent."""
    out = {}
    try:
        o += 1 + 8 * 4                                       # track_volume, unclaimed, claimed, sol volume, last update
        n = struct.unpack_from("<I", raw, o)[0]; o += 4
        out["ix"] = raw[o:o + n].decode(errors="replace"); o += n
        out["mayhem"] = bool(raw[o]); o += 1
        out["cashback_bps"], out["cashback"] = struct.unpack_from("<QQ", raw, o); o += 16
        out["buyback_bps"], bb = struct.unpack_from("<QQ", raw, o); o += 16
        out["buyback"] = bb / 1e9
        out["cashback"] = out["cashback"] / 1e9
        k = struct.unpack_from("<I", raw, o)[0]; o += 4 + 34 * k
        out["quote_mint"] = b58.encode(raw[o:o + 32]); o += 32
        qa, vq, rq = struct.unpack_from("<QQQ", raw, o); o += 24
        out.update(quote_amount_raw=qa, vquote_raw=vq, rquote_raw=rq)
        out["holder_rewards_bps"] = struct.unpack_from("<Q", raw, o)[0]
    except Exception:
        pass
    return out


def migrated(raw):
    if len(raw) < 8 + 192 or raw[:8] != MIGRATED:
        return None
    d = raw[8:]
    return {"user": b58.encode(d[0:32]), "mint": b58.encode(d[32:64]), "pool": b58.encode(d[128:160]),
            "quote_mint": b58.encode(d[160:192]), "ts": struct.unpack_from("<q", d, 120)[0]}


def postbuy(raw):
    if len(raw) < 8 + 224 or raw[:8] != POSTBUY:
        return None
    d = raw[8:]
    v = struct.unpack_from("<QQQQQQQQQQQ", d, 136)
    return {"user": b58.encode(d[0:32]), "mint": b58.encode(d[32:64]), "ts": struct.unpack_from("<q", d, 128)[0],
            "tok": v[0] / 1e6, "sol": v[1] / 1e9, "fee_bps": v[2], "fee": v[3] / 1e9, "cfee_bps": v[4],
            "cfee": v[5] / 1e9, "buyback": v[6] / 1e9, "pool_base_after": v[9], "pool_quote_after": v[10]}


def amm_trade(raw):
    """PumpSwap BuyEvent/SellEvent -> dict with effective reserves (quote incl. signed virtual_quote_reserves)."""
    if raw[:8] not in (AMM_BUY, AMM_SELL) or len(raw) < 8 + 352:
        return None
    buy = raw[:8] == AMM_BUY
    d = raw[8:]
    ts, base_amt = struct.unpack_from("<qQ", d, 0)
    pb, pq, qamt = struct.unpack_from("<QQQ", d, 40)
    lp_bps, lp_fee, pr_bps, pr_fee = struct.unpack_from("<QQQQ", d, 64)
    user_q = struct.unpack_from("<Q", d, 104)[0]
    pool, user = b58.encode(d[112:144]), b58.encode(d[144:176])
    cc_bps, cc_fee = struct.unpack_from("<QQ", d, 336)
    vq = 0
    try:
        if buy:
            o = 393
            n = struct.unpack_from("<I", d, o)[0]; o += 4 + n
            o += 32                                           # cashback bps/amt, buyback bps/amt
            vq = int.from_bytes(d[o:o + 16], "little", signed=True)
        else:
            vq = int.from_bytes(d[384:400], "little", signed=True)
    except Exception:
        pass
    return {"ts": ts, "pool": pool, "user": user, "buy": buy, "tok": base_amt / 1e6, "sol": qamt / 1e9,
            "user_sol": user_q / 1e9, "pool_base_raw": pb, "pool_quote_raw": pq, "vquote_raw": vq,
            "fee_bps_total": lp_bps + pr_bps + cc_bps, "lp_bps": lp_bps, "protocol_bps": pr_bps, "creator_bps": cc_bps}


def amm_create(raw):
    if len(raw) < 8 + 197 or raw[:8] != AMM_CREATE:
        return None
    d = raw[8:]
    return {"base_mint": b58.encode(d[42:74]), "quote_mint": b58.encode(d[74:106]), "pool": b58.encode(d[165:197])}


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
        for kind, fn in (("complete", complete), ("migrated", migrated), ("postbuy", postbuy),
                         ("amm_trade", amm_trade), ("amm_create", amm_create)):
            v = fn(raw)
            if v:
                out.append((kind, v)); break
    return out
