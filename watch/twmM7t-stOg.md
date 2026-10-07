# Watched: https://www.youtube.com/watch?v=twmM7t-stOg

model `gemini-3.7-flash` · tokens in 89336 out 3122

Here is an objective, critical breakdown of the video’s on-screen data, trading methodology, evidence quality, and logical risks.

---

### 1. What’s On Screen (Visual Details Not Fully Captured by Audio)

* **Trading Terminal / UI**: The platform used is **Axiom Trade** (`axiom.trade/pulse?chain=sol`) connected to a Solana wallet (Phantom).
* **00:03**: Starting balance shown in Phantom wallet: **0.10006 SOL** ($13.89 USD).
* **00:33–01:19**: Axiom Pulse dashboard layout:
  * Columns: *New Pairs*, *Final Stretch*, *Migrated*, and a right-hand *Tracker/Live Trades* feed.
  * Presets visible: Quick buy presets (e.g., `0.07 SOL`, `P1`, `P2`, `P3`).
* **01:56–02:00**: Quick-buy UI shows setting preset buy to **0.07 SOL** with priority fee / MEV options.
* **02:37–03:01 (Trade 1 - CWM / Collective Wealth Magic)**:
  * **Chart Timeframe**: 1-second (`1s`) candle chart on `axiom.trade`.
  * **Entry**: Buy marker `B` on bonding curve chart at initial pump right after @truth_terminal tweet match. Bought: 0.07 SOL ($9.726).
  * **Exit**: Sold at top green wick for 0.138 SOL ($19.16). PnL: **+0.068 SOL (+97%)** / +$9.432.
  * **Wallet Balance**: 0.15 SOL shown on screen (02:48).
* **03:20–03:34 (Trade 2 - 67 / 672)**:
  * **Chart Timeframe**: 1-second candles.
  * **Entry**: Bought 0.1 SOL ($14k MC).
  * **Exit**: Sold at 0.213 SOL. PnL: **+0.113 SOL (+113%)**.
  * **Updated Balance displayed**: **0.262 SOL** (03:34).
* **03:50–04:35 (Trade 3 - 67 Community / "7")**:
  * **Chart**: 1-second candles, Axiom order panel with multi-preset buttons (0.05, 0.08, 0.1, 0.25 SOL; Sell 25%, 50%, 75%, 100%).
  * **Entry**: Bought 0.2 SOL at ~$20k MC.
  * **Exit**: Dump candle down to cost basis; sold to break even (`S` marker at entry cost line). PnL: ~0.00 SOL net.
* **04:36–05:14 (Trade 4 - Y2K2)**:
  * **Chart**: 1-second candles. Bubble map icon checked.
  * **Entry**: Bought 0.2 SOL at ~$33k MC.
  * **Exit**: Choppy consolidation; sold 0.303 SOL at ~$38k MC. PnL: **+0.103 SOL (+52%)**. Balance: **0.32 SOL** (05:03).
* **05:16–05:58 (Trade 5 - pwease2)**:
  * **Chart**: 1-second candles.
  * **Entry**: Scale-in buys (`B`, `DB` markers) at bottom consolidation (~$13k–$15k MC). Total bought: 0.3 SOL.
  * **Exit**: Sold at resistance line ($24.3k MC). Sold: 0.619 SOL. PnL: **+0.319 SOL (+106%)**.
  * **Updated Balance displayed**: **0.639 SOL** (05:58).
* **06:18–07:11 (Trade 6 - ym / young male)**:
  * **Chart**: 1-second candles. Holder bubble map / Top 10 holder tab: Top 10 hold 29.5%, Dev holds 0%, Snipers hold 1%.
  * **Entry**: Bought 0.507 SOL at ~$15k MC.
  * **Exit**: Sold around $30.2k MC due to large holder dumping risk. Sold: 0.994 SOL. PnL: **+0.487 SOL (+96%)**.
  * **Updated Balance displayed**: **1.006 SOL** (07:02).
* **08:24–10:25 (Trade 7 - TYCOON)**:
  * Trade partly happened off-recording due to disk storage error.
  * **Chart**: Multiple laddered buy markers (`B`) from ~$33k to $40k MC.
  * **Token info panel**: Top 10 hold 20.67%, Dev holds 3.15%, Snipers hold 3.17%.
  * **Exit**: Sudden red dump wick ("crime candle"); sold remaining bag for 1.619 SOL. Total Bought: 1.006 SOL. PnL: **+0.613 SOL (+61%)**.
  * **Updated Balance displayed**: **1.608 SOL** (10:21).
* **10:38–11:37 (Trade 8 - 95 / The Official 95 Coin)**:
  * **Chart**: 1-second candles. Bubble map inspected (dense clustering).
  * **Entry**: Bought 0.507 SOL at ~$15k MC.
  * **Exit**: Sold at breakout to ~$26k MC. Sold: 0.994 SOL. PnL: **+0.487 SOL (+96%)**.
  * **Updated Balance displayed**: **2.094 SOL** (11:35).
* **12:09–12:58 (Trade 9 - A / A Coin)**:
  * **Chart**: 1-second candles.
  * **Entry**: Bought 0.5 SOL at ~$21k MC.
  * **Exit**: Failed breakout; dumped below entry line. Sold at market for 0.473 SOL. PnL: **-0.034 SOL (-4%)**.
  * **Updated Balance displayed**: **2.04 SOL** (12:51).
* **13:10–13:46 (Trade 10 - cap)**:
  * **Chart**: 1-second candles. Scalped multiple buys on rebound after dump.
  * **Entry**: Total bought 1.111 SOL ($153.20).
  * **Exit**: Sold 1.65 SOL ($228.40). PnL: **+0.539 SOL (+49%)**.
  * **Updated Balance displayed**: **2.576 SOL** (13:43).
* **13:55–14:40 (Trade 11 - GOONER)**:
  * **Chart**: 1-second candles.
  * **Entry**: Bought 0.505 SOL at ~$10k MC.
  * **Exit**: Rapidly micro-sold across peak using "1-cent buy/sell" spam strategy. Sold 1.098 SOL. PnL: **+0.593 SOL (+118%)**.
  * **Final Balance displayed**: **3.054 SOL** (14:39).

---

### 2. Concrete Trading Rules

| Rule Category | Description | Exact Parameter / Condition | Timestamp | Bot Testable? |
| :--- | :--- | :--- | :--- | :--- |
| **Sizing / Progression** | Compound small balance by risking large portfolio fraction per trade (50% to 100% of balance minus gas reserve). | Start 0.07–0.10 SOL $\rightarrow$ 0.2 SOL $\rightarrow$ 0.3 SOL $\rightarrow$ 0.5 SOL $\rightarrow$ 1.0 SOL. | 00:53, 01:58, 07:23 | **Yes** |
| **Entry (Narrative Snipe)** | Snipe newly launched pump.fun pairs corresponding to viral Twitter/X events or influential accounts (e.g., Terminal of Truths). | Matching token deploy within $\le 5$ seconds of tweet; Buy preset = fixed SOL. | 02:26–02:40 | **Partly** (Requires Twitter scrape + keyword regex + instant RPC buy). |
| **Entry (Dev Track Record)** | Enter tokens launched by developers whose previous tokens reached high market caps (e.g., >$300k MC). | Verified deployer wallet history. | 05:20 | **Yes** (On-chain deployer profiling). |
| **Entry (Paid Dex / KOL Buy)** | Enter when DexScreener/Dex banner is paid and a verified high-follower influencer (>100k followers) retweets/posts contract address (CA). | Dex banner paid status = true; CA tweeted by specific whitelisted handle. | 09:46–09:56 | **Partly** (Requires API monitoring for Dex paid ads + Twitter API). |
| **Entry (Dip / Support Re-bid)** | Buy consolidation floors after initial launch dump if liquidity/floor holds. | Price tests average cost basis / lower range on 1s chart and prints higher low. | 05:29, 13:30 | **Partly** (Discretionary chart pattern on 1-second timeframe). |
| **Exit (Target Profit)** | Liquidate position upon doubling initial investment. | Target: **+100% PnL (2x)** or manual partials starting at +50% to +100%. | 00:56, 03:01 | **Yes** (Automated limit/take-profit trigger). |
| **Exit (Stop Loss / Breakeven)** | Cut position immediately as soon as price reverts to the average entry price. | Price $\le$ Average Entry Price $\rightarrow$ Market Sell 100%. | 00:34–00:49, 04:08 | **Yes** (Trailing/breakeven stop loss). |

---

### 3. Evidence Quality

* **What is Verified on Screen**:
  * Actual trading UI interactions on Axiom Trade terminal with real-time DOM/chart updates, transaction confirmation toasts, and Phantom balance increments.
  * Real order placements displaying entry prices, exit prices, and percentage PnLs inside the Axiom token manager widget.
* **What is Missing / Unverified**:
  * **Solscan transaction hashes** were not opened to verify net fees, gas tip costs, slippage penalties, and MEV frontrunning deductions.
  * **Trade 7 (TYCOON)** had its entry cut off due to an alleged screen recording software/storage crash (08:24), meaning the full timeline of that trade was not shown continuously.
* **Commercial / Promotional Ties**:
  * The creator provides referral links to **Axiom Trade** and **Nova Trade** in the video description and actively promotes them at 15:57–16:03.
  * Promotes his own Discord community, giveaways, and previous video course (00:07, 01:28, 11:52).

---

### 4. Contradictions & Systemic Risks

1. **Illusion of the "Strict Breakeven Stop Loss" on Microcaps**:
   * The creator claims Rule #1 is "cutting losses as soon as they come down to average price" to avoid any drawdown (00:34).
   * *Reality/Systemic Risk*: On Pump.fun bonding curves with micro-liquidity ($4k–$20k market caps), a single developer dump or whale exit removes liquidity instantly. A market sell order submitted at breakeven often experiences 20%–80% negative slippage or fails due to block congestion, making zero-loss trading unviable in automated execution over large sample sizes.
2. **Full-Port Compounding Flaw**:
   * Sizing 50%–100% of an entire account into brand-new meme pairs (00:57) has a mathematical certainty of total account wipeout ($P(\text{ruin}) = 1.0$) upon encountering a single un-sellable honeypot, blacklisted token, or instant 100% rug pull.
3. **Target Discrepancy**:
   * Video title and intro claim aiming for **$500** starting from 0.1 SOL (~$14) (00:05).
   * Trading was halted at **3.054 SOL** (~$425 at the depicted ~$139/SOL rate) (14:39), at which point the creator arbitrarily decided to "stop here" (14:55) rather than completing the stated mathematical sequence to $500.
4. **Execution Survivorship**:
   * Out of 11 trades, 9 were profitable, 1 broke even, and 1 lost 4%. This win rate (>80%) on sub-1-minute holding times on microcap memecoins represents extreme positive variance / cherry-picked recording session, which is unsustainable without survivor bias.
