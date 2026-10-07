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
