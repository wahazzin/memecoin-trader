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

## 2026-10-07 — Paper trading goes through Jupiter (a real trading API), not our own math

Owner requirement: paper trades must come from a real platform, nothing assumed or modelled.
Searched for a memecoin trading platform with an API + paper mode. Found: browser-only paper tools
(PaperApe, MockApe, Meme Paper, Target, Aped) with **no bot API**; exchange testnets (Binance, Bybit,
Hyperliquid) that don't list fresh memecoins. None fits.

**Jupiter** (the swap router behind Axiom/Photon/Phantom swaps) has a free **quote API**: "swap X SOL
into this coin right now → you get exactly Y tokens", routed through the real pools, including
pump.fun's own fees and price impact. Probe 3 (2026-10-07 20:01 UTC, read-only):

- ✅ quotes for **brand-new pump.fun coins (~6 min old)**, routed via "Pump.fun"; and for migrated coins
  via "Pump.fun Amm".
- Buying 0.1 SOL and selling straight back = **−3.1% round trip** on most coins (fees + impact), up to
  −8% on thinly routed ones. Two coins had no sell route at that moment (a real-world risk too).
- Rate: ~18 successful quotes/second from one runner, plenty.

**Decision:** every paper buy and sell = a live Jupiter quote at that exact moment for that exact size;
the paper fill is the quote's output amount. The one thing no paper trading can show (Alpaca's
included): whether a real order would have landed before competing bots. That stays stated, not modelled.

## 2026-10-07 — Costs measured from real transactions; bonding-curve formula verified exactly

**Costs** (`research/measure_costs.py`, 178 real trades split into every SOL paid): pump.fun + creator fee
1.25% per side on standard coins; creator fee is 1–3% on ~2% of coins; priority fee median 0.00005 SOL
(p90 0.0015–0.003); new-account rent ~0.002 SOL on 60–90% of first buys; ~1% "unexplained" on terminal
users (terminal fees). All-in: ~4.5–5% round trip on 0.1 SOL, ~3% on 0.5 SOL. Details in COST_FACTORS.md.

**Formula check** (`research/check_formula.py`, verdict rule fixed before running: median ≤ 0.1%, worst
≤ 0.5%): our bonding-curve formula vs live Jupiter quotes on 43 coin/size pairs with unchanged reserves:
**0.0000% difference, buy and sell, at 0.1 / 0.5 / 2 SOL. PASS.** Backtests on recorded data can price
fills with the formula and get exactly what Jupiter would have quoted at that moment. (Coins that
graduated to PumpSwap use a different pool; they need their own check before being backtested.)

## 2026-10-08 — Live paper bot v0.1 switched on (after 4 smoke tests)

Spec: BOT_SPEC.md. Arms `m1_pass` (all Setuh checks pass at the M1 checkpoint) vs `m1_random` (random 10%
of all checkpoint coins). Fills: live Jupiter quotes (worse of two, 2 s apart) + measured costs; sells
that Jupiter can't route are priced from the coin's on-chain curve (marked). Circuit breaker 15%/day/arm.
Smoke tests found and fixed 3 bugs (see BOT_SPEC.md). Key observation: at the checkpoint, prices swing
±50% within 2 seconds, so stops fill far below −20% on dumps. Results only count after 6+ weeks.

## 2026-10-08 — Gemini watched 17 of 19 Setuh videos; M2 pre-registered

**What the screen adds** (Gemini notes, synthesized; Gemini itself made arithmetic errors, so any number
used gets checked against the frame first): his own wallet or full trade history is **never** shown;
P&L proof is cropped promo cards with referral links; on-screen realized losses −36%, −52%, −74% despite
a "−20% stop"; on-screen bet sizes 50–100% of the account (he says 10–25%); filter values change between
videos and even between screen and his own Discord card. **No live trade is provably a 40–50% dip entry**:
that rule rests on hindsight charts only.

**M2** (`research/M2_PREREG.md`): 40–50% dip from a local high ≥ 5× launch, first buy back in the band,
+100% / −20% (filled at the next real trade) / 15 min / 60 min, vs a random-entry control on the same coins.
Code validated on synthetic data: planted effect → PASS; no effect → NO EVIDENCE. Lesson from the
synthetic null: dip entries "beat random" even with no edge (random includes buying tops), so the
absolute after-cost expectancy criterion is essential.

## 2026-10-08 — First night of the paper bot + M1b data collection started

Overnight (~10 h, NOT evidence): `m1_pass` 79 closed trades, 23% wins, expectancy −0.075 SOL/trade;
`m1_random` 37 trades, 11% wins, −0.161 SOL/trade. Both arms hit the 15%/day circuit breaker (4 times in
total). 53 sells had to be priced from the on-chain curve because Jupiter had no route.

Started recording **who funded each checkpoint coin's top 10 holders** (wallet age, transaction count,
first funder, funding time) into `funding.jsonl`, for a later pre-registered test M1b. Recorded only, not
used for trading. Weekly report snapshots now saved every Monday in `weekly/` on `paper-state`.
Fixed: the backup cron could start a second recorder in parallel; now it only starts one when none runs.

## 2026-10-08 — Owner: "are you sure there's nothing to add?" → found 3 real gaps (read pump.fun's official docs)

Read all of pump.fun's public docs + IDLs and checked the open questions on live data (`research/probe_full.py`):
- **Graduated coins were invisible**: after migration they trade on PumpSwap (a different program). Now recorded,
  followed by the bot, and used by M1/M2 (amendment A2). PumpSwap pool reserves in events are BEFORE the trade
  (13,306 of 13,306 consecutive pairs).
- **Non-SOL coins (~1% of trades) had price 0** → could pass the live bot's checkpoint test (bug). Now excluded.
- **Fees after graduation vary 0.30–1.25% by market cap** (COST_FACTORS #19). Buyback is part of the 0.95%, not extra (#21).
Also: holder-reward and cashback coins exist (cost unchanged / rebate, conservative = ignore rebate).
