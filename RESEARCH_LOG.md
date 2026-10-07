# RESEARCH LOG — memecoin-trader

## 2026-10-07 — Source study: Setuh (YouTube @setuhh), all 19 videos

Transcripts pulled with `crypto-ai-trader/tools/yt_learn.py` from the owner's PC (YouTube blocks
cloud servers). Full notes: project doc `claude/project3_setuh_research.md`.

**Verdict:** good teacher of how the trenches work; **not evidence**. No wallet, no trade log, every
example is a winner picked afterwards, referral links in every video, rules contradict across videos.
His own "realistic results" videos (~47 trades): ~77% win rate but average loss ≈ average win, and
the biggest loss (−5.2 SOL) beat the biggest win (+3.8). His edge is mostly **rug avoidance**.

**Candidate rules to test (hypotheses):** Pump.fun only; age ≤ 40 min, dev ≤ 5%, insiders ≤ 20%;
no holder > 4%; top holders not funded from the same place at the same time and not holding equal
SOL; no single dev-buy candle to ~10k; buy a 40–50% drop from a local high ≥ ~15k; stop −20%,
take profit +50–100%, exit after ~15 min with no volume.

## 2026-10-07 — Data probes (read-only, from GitHub's servers)

| Source | Works? | What it gives |
|---|---|---|
| PumpPortal websocket | ✅ new coins (~45,000/day) + migrations (~1/min) | Trade stream needs an API key funded with 0.02 SOL → **not needed**, see next row |
| **Solana public RPC `logsSubscribe` on the pump.fun program** | ✅ **free, no key** | **Every pump.fun trade** (~5.6M/day) decoded from TradeEvent: coin, buyer/seller wallet, SOL size, buy/sell, time, bonding-curve reserves (= exact price). ~11% of events decode as zero-size (to investigate in the recorder) |
| GeckoTerminal | ✅ | 1-minute OHLCV for migrated (PumpSwap) pools, 1,000 candles per call |
| DexScreener | ✅ | Token pairs incl. brand-new pump coins; "paid profile" feed |
| pump.fun frontend API | ❌ 404 | Not needed |

**Decision:** build our own recorder on the free trade stream. Recording forward (instead of buying
historical data) also removes survivorship bias and lookahead: we see every coin, including the
~99% that die, exactly as it looked at the time.

## 2026-10-07 — Recorder live + first measurements

**No paper-trading platform exists for pump.fun** (only browser extensions like DryFlip / GhostTrade for
manual clicking, which also simulate on live prices). Owner decision: we build our own. Paper fills will
use the live on-chain reserves at the moment of the order (pump.fun's price is a public formula), so a
paper fill = what the real market would have given at that instant. No invented slippage numbers:
delays and costs will be **measured** from our own recorded data (how fast prices move between seconds,
real fees from the events).

**Measured from the first hour of recording:**
- ~41,000 trades in 11 minutes (~5.4M/day), ~440 new coins per 11 min.
- **Real pump.fun fees, read from the trade events: 0.95% protocol + 0.30% creator = 1.25% per side,
  2.5% per round trip** before priority fees. Every scalp has to beat that.
- The free public Solana connection drops every 1–2 min and reconnects in ~2 s. Gaps are logged in
  every hour's `status` file, never hidden. If gaps turn out to matter, a free Helius key is the fix.
- Bug found and fixed: hour files flip-flopped at the hour boundary because of late trades and
  overwrote each other. Fixed (forward-only roll, unique file names), recorder restarted.

**Gemini "watch" tool works** (`tools/watch.py`, action `watch`): Gemini watches the actual video.
First test (Setuh, ponzi video) caught on-screen facts the transcript can't: 5-second chart, every Axiom
safety filter left off, 4.22 SOL balance, no trade history shown.
