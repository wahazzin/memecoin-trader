# Watched: https://www.youtube.com/watch?v=Uh1j4sfnfSI

model `gemini-3.8-flash` · tokens in 82688 out 2147

# Analysis & System Engineering Notes: Memecoin Masterclass Pt. 1

---

## 1. On-Screen Data & Visual Inspection (Beyond Narration)

### P&L Claims & Proof Verification
- **00:00 & 04:36**: Balance progression banners displayed:
  - Slide 1 banner: `$87.88 (-$11.69, -11.74%)` $\rightarrow$ `$106,221.02 (-$32,681.03, -21.93%)`.
  - Slide 5 banner: `$87.87` $\rightarrow$ `$10,934.25`.
  - **Verification Status**: Zero transaction hashes, zero public Solana wallet addresses, and zero uncropped platform dashboards are provided. These are isolated, cropped graphic snippets with no verifiable on-chain audit trail.

---

### Strategy 1: High Market Cap Scalping Filter Panel (07:41 – 10:11)
The trading terminal filter screen (BullX/Photon-style interface) displays exact parameters that diverge from the audio commentary:
- **Filter Settings on Screen**:
  - `Dev holding %`: Max `11%`
  - `Insider wallets supply %`: Max `10%`
  - `Volume`: Min `$90,000`
  - `Market Cap`: Min `$75,000` (Note: audio text says "1–5M Market Cap", but the filter input explicitly sets `$75,000`)
  - `Token Age (min)`: Min `120` minutes
- **Chart Inspection (08:12 – 10:11)**:
  - **Timeframe**: 3-minute candlestick chart (confirmed visually and verbally at 08:41).
  - **Overlay / Annotations**: 
    - Previous ATH level marked.
    - Retracement measurement tool measuring drop from ATH: `-35%`, `-50.52%`, and `-65%`.
    - Market cap level at entry on chart: `~707.09K`.
    - Marked entry: First green reversal candle after printing a -50% retracement.

---

### Strategy 2: "About to Graduate" Pump.fun Filter Panel (10:12 – 12:32)
- **Filter Settings on Screen**:
  - `Dev holding %`: Max `0%`
  - `Insider wallets supply %`: Max `25%`
  - `Bot users`: Min `10`
  - `Market Cap`: Min `$15,000`
  - `Token Age (min)`: Min `30` minutes
- **Transaction Stream Comparison ("Real" vs "Fake" at 10:12 – 12:18)**:
  - **Fake/Bot Stream**: Shows uniform buy patterns accompanied by wallet tags (blue/yellow badges, top holder badges, and volume bot/bundler patterns).
  - **Real Stream**: Shows organic distribution across varying tiers (shrimp, fish, dolphin tiers) with distinct wallet addresses and absence of top-holder concentration flags.
- **Chart Inspection (11:08 – 11:35)**:
  - **Timeframe**: 1-minute candlestick chart (verified at 11:23).
  - Visual setup: Clean breakout to ATH $\rightarrow$ -50% dip $\rightarrow$ entry upon appearance of consecutive green candles.

---

## 2. Concrete Trading Rules & Automation Feasibility

| Rule Description | Exact Parameters | Timestamp | Bot Automatable? | Logic / Automation Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Position Sizing** | Risk 10% to 30% of total portfolio balance per trade (specifically 0.1 SOL on a 1.0 SOL balance). | 05:24 | **Yes** | `Order_Size = Portfolio_Balance * 0.10` |
| **Stop-Loss Cut** | Fixed stop-loss at -20% PnL. Mental or hard stop; round-tripping prohibited. | 06:16, 12:33, 14:10 | **Yes** | `Exit if Position_PnL <= -0.20` |
| **Take-Profit Execution** | Full position exit ("Full Clip") at +30% to +50% PnL (or 2x / +100% on breakout momentum). Partial profit-taking explicitly prohibited. | 06:58, 07:41, 10:12 | **Yes** | `Exit 100% if Position_PnL >= 0.35` |
| **New Token Avoidance** | Blacklist tokens directly at creation; trade only established/graduated tokens. | 05:02 | **Yes** | `Filter: Token_Age >= 30m` or `120m` |
| **High MC Scalp Filter** | Age $\ge$ 120m, Vol $\ge$ $90k, MC $\ge$ $75k, Dev $\le$ 11%, Insiders $\le$ 10%. | 07:41 | **Yes** | Direct API filter against DexScreener/BullX endpoints. |
| **High MC Scalp Entry** | Token broke prior ATH $\rightarrow$ pulls back by 35%, 50%, or 65% $\rightarrow$ entry on first green candle close. | 08:04 – 08:48 | **Partly** | ATH calculation and dip percentage are simple; detecting candle color reversal is trivial, but volume/rejection context requires heuristic rules. |
| **Graduate Filter** | Age $\ge$ 30m, MC $\ge$ $15k, Dev holding = 0%, Insiders $\le$ 25%, Bot users $\ge$ 10. | 10:21 | **Yes** | Direct query to Pump.fun contract state / bonding curve progress. |
| **Real Volume Filter** | Exclude tokens where transaction stream is dominated by flagged bundle/volume bots. | 11:53 – 12:28 | **Partly** | Requires wallet profiling: clustering buy sizes and checking insider/top-holder tags. |
| **Post-Trade Discipline** | Close chart immediately after selling; no re-entries on runner FOMO. | 06:40, 09:35 | **Yes** | Set cooldown period per token: `Token_Blacklist_Duration = 24h` post-exit. |
| **Circuit Breaker** | Stop trading after 4–5 consecutive losses. | 13:54 | **Yes** | `If Consecutive_Losses >= 4: Halt_Trading(duration)` |

---

## 3. Evidence Quality & Transparency

- **Verification Level**: **Extremely Low**.
  - All balance figures (`$87` to `$106k`, `$87` to `$10.9k`) are static image overlays.
  - No live trade executions, screen recordings of orders submitting, or Solana Explorer/Solscan transaction hashes are provided.
- **Cherry-Picking**:
  - The chart examples (08:12 and 11:08) show selective hindsight entries where dip-buys bounced for 60%–200% gains.
  - Failed dip setups (tokens dipping 50% and continuing down to 0) are not demonstrated on charts despite the presenter stating "most coins rug."
- **Monetization & Affiliations**:
  - Standard engagement funnel (calls to subscribe for "Part 2" masterclasses).
  - Terminal shown is BullX/Photon format, commonly tied to referral-link monetization.

---

## 4. Contradictions & Critical System Flaws

1. **Market Cap Metric Conflict**:
   - The on-screen text and audio state: *"Scalping high market caps (1M - 20M)"* and *"1-5M Market Cap"* (07:41).
   - The actual screener filter input on the same screen shows: `Market Cap: 75000` ($75k) minimum (07:41). A $75k coin behaves completely differently in liquidity, slippage, and volatility compared to a $1M–$5M asset.

2. **Full Clip vs. Slippage & High Balance Disconnect**:
   - The rule explicitly mandates: *"Never take initials always full clip"* (04:36, 06:58) to avoid fee drag on small accounts ($10–$100).
   - However, the author presents a claimed account size of `$106,221.02`. Dumping 100% of a large position in a low-liquidity memecoin pool creates severe negative price impact. A rule designed for tiny accounts directly conflicts with portfolio scaling.

3. **Re-Entry Prohibition vs. Multi-Dip Structure**:
   - At 06:40 and 09:35, the rule insists: *"As soon as you sell, click off the coin... do not sit and watch the chart."*
   - Yet at 08:59, the presenter praises trading the exact same coin across multiple sequential dips (*"It happened again... another 75% PnL"*). An automated system cannot simultaneously forbid watching a token post-sale while expecting to catch secondary dip bounces on the same chart.
