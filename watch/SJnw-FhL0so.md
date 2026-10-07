# Watched: https://www.youtube.com/watch?v=SJnw-FhL0so

model `gemini-3.7-flash` · tokens in 112273 out 2257

Here are the detailed markdown notes analyzing the trading video, on-screen data, mechanics, and algorithmic rule feasibility:

---

### 1. What’s on Screen (Platform & UI Details)

* **Platform / Interface**:
  * **Trading Terminal**: Padre Terminal (`trade.padre.gg` / Padre Terminal for Solana meme coins/Pump.fun).
  * **Interface Panels**:
    * **Trenches Dashboard** (`00:05`, `03:22`, `14:09`): 3 columns — *New*, *Soon* (bonding curve nearing migration), and *Migrated* (Raydium pools).
    * **Terminal Token Data Panel** (`03:54`, `04:46`, `17:00`): Shows Token Name/Ticker, Market Cap ($), Liquidity ($), Supply (1B standard Pump.fun tokens), 24h/5m Volume, Top 10 Holders %, Dev Holding %, Insiders %, Sniper count, Fresh Wallet %, Bundled Supply Bubble Maps (`12:59`, `13:00`), and Dev History badges.
    * **Execution Module**: Buy presets (0.1, 0.2, 0.5, 1, 2 SOL / Custom), Sell presets (25%, 50%, 75%, 100%, Sell Initial), Slippage/Priority Gas settings (`Instant Trade` toggle, variable gas fees 0.001–0.01 SOL).
* **Chart Settings**:
  * **Timeframes**: Highly granular sub-minute charts (`1s` candles at `03:51`, `1m` candles at `10:22`, `14:38`, `17:00`).
  * **Indicators**: Clean candlestick view without moving averages or standard oscillators; on-chart buy (green dots) and sell (red/orange dots) execution markers overlaid directly on the price curve.
* **Account / Wallet Proof**:
  * Wallet tag shown: `setuh` / `SetWifiBread` (`00:02`).
  * Public Solana wallet address is partially hidden/truncated in the UI (e.g., `BGd5D...pump` or token mints shown, but master public key is not fully displayed in plaintext).
  * Real-time balance updates in Padre wallet header: `1.000 SOL` (`03:23`) $\rightarrow$ `2.349 SOL` (`06:35`) $\rightarrow$ `2.697 SOL` (`08:22`) $\rightarrow$ `3.878 SOL` (`10:07`) $\rightarrow$ `5.967 SOL` (`11:48`) $\rightarrow$ `6.53 SOL` (`12:48`) $\rightarrow$ `7.747 SOL` (`14:10`) $\rightarrow$ `11.44 SOL` (`16:11`) $\rightarrow$ `6.20 SOL` (`18:57`).

---

### 2. Concrete Trading Rules & Automation Feasibility

| Rule Type | Parameters & Logic | Video Timestamp | Automatable? (Bot Data Check) |
| :--- | :--- | :--- | :--- |
| **Phase 1 Sizing** | Allocate $0.25\text{ SOL}$ to $1.0\text{ SOL}$ (approx. $10\%\text{--}40\%$ of initial sub-portfolio) per trade until balance $\ge 10\text{ SOL}$. | `03:29`, `04:46`, `08:27` | **Yes** (Strict mathematical sizing rule). |
| **Phase 2 Sizing (Full Port Bet)** | Once portfolio hits $\ge 10\text{ SOL}$, commit exactly $10\text{ SOL}$ into a single token. | `00:17`, `16:17`, `17:24` | **Yes** (Fixed milestone sizing logic). |
| **Entry Filter: Narrative / "Tech Meta"** | Manually filtering for trending Pump.fun meta themes: bonding curve utilities, Telegram launchpad/bot clones (`PBANK`, `NEW`), 4chan memes (`Simon`, `WHEPE`), or viral news/AI gambling (`AI`). | `04:49`, `08:34`, `14:48`, `17:02` | **No** (Qualitative narrative discretion based on social hype). |
| **Entry Filter: Token Safety / Bundles** | Screen for dev supply lock/burn, sniper concentration, and bubble map bundle clustering. (Note: He bypassed high bundle risk on `AUTISM` at `12:58` purely on momentum). | `04:26`, `12:58` | **Partly** (Bubble map API/top 10 holder % is parseable, but discretionary override occurred). |
| **Take-Profit: Scaling / Take Initial** | Click "Sell Initial" (recouping 100% principal) when trade reaches $+100\%$ ($2\times$) or take partials ($25\%\text{--}50\%$) on parabolic micro-structure pumps. | `09:07`, `11:05`, `15:40` | **Yes** (Rule-based limit triggers on PNL thresholds). |
| **Exit Trigger: Churn / Volume Stall** | If a token experiences repeated KOL buy-spikes immediately followed by instant 100% sell-offs ("bought up, sold off" choppy churn) and volume declines, execute full market exit. | `07:40`–`08:12`, `12:49` | **Partly** (Can track tick-level order flow imbalances and buy-to-sell velocity). |
| **Stop Loss (Full Port Bet)** | Hard cut at $-50\%$ unrealized drawdown ($5\text{ SOL}$ max loss on a $10\text{ SOL}$ entry). | `00:35`, `17:31`, `18:53` | **Yes** (Strict trailing/fixed percentage stop order: sold at $-52.7\%$ / $-5.27\text{ SOL}$). |

---

### 3. Evidence Quality & Promotion Context

* **Verified On-Screen**:
  * Real-time UI trade execution and on-screen PnL tracking for 7 distinct trades:
    1. `Liquid/SOL`: $+0.21\text{ SOL}$ ($+24\%$)
    2. `PBANK/SOL`: $+1.156\text{ SOL}$ ($+114\%$)
    3. `WHEPE/SOL`: $+0.277\text{ SOL}$ ($+27\%$)
    4. `niggapad/SOL`: $+1.192\text{ SOL}$ ($+115\%$)
    5. `NEW/SOL`: $+2.038\text{ SOL}$ ($+133\%$)
    6. `AUTISM/SOL`: $+0.737\text{ SOL}$ ($+72\%$) $\rightarrow$ `RAWDOG/SOL`: $+1.187\text{ SOL}$ $\rightarrow$ `Simon/SOL`: $+3.81\text{ SOL}$
    7. `AI/SOL`: $-5.273\text{ SOL}$ ($-52.2\%$)
  * Net result shown: Balance grew from $1.0\text{ SOL}$ $\rightarrow$ $11.44\text{ SOL}$ $\rightarrow$ $6.20\text{ SOL}$.
* **Claimed vs. Unverified**:
  * The total time spent was claimed to be within 24 hours (clock timestamps in UI confirm executions occurred within the same evening session).
  * Proof of mobile trading while away from desk (`15:34`) was shown via an unverified overlay photo and mobile screenshot.
* **Commercial Interests & Affiliations**:
  * Active promotion of his personal Discord server ("PF Trenches") and an "Elite" tier (`01:03`–`02:07`).
  * Funnel mechanism: Requires users to deposit $\$50$ into their platform wallet to gain elite access/tracker tools.
  * Active streaming promotion for his Twitch live streams.

---

### 4. Contradictions, Red Flags & Algorithmic Realities

1. **Systemic Negative Expectancy of the "All-In / Full Port" Rule**:
   * Stacking micro-wins from $1\text{ SOL}$ to $11.44\text{ SOL}$ through multiple low-cap scalps, only to risk $88\%$ of the account ($10\text{ SOL}$) on a single coin at an all-time-high breakout (`17:23`), creates an extreme risk-of-ruin profile. In an algorithmic setup, this bet sizing wipe-out condition destroys compound growth.
2. **Execution Slippage & Hidden Costs**:
   * On sub-minute 1-second candles with micro-caps under $\$100\text{k}$ liquidity, executing market orders with high priority gas ($0.001\text{--}0.01\text{ SOL}$) across numerous round-trips adds significant drag that becomes fatal if hit rates drop below $70\%$.
3. **Discretionary Rule Deviation**:
   * The video states a rule to avoid heavily bundled tokens or dev dumps, yet he explicitly entered `AUTISM` despite noting the bubble map was "bundled to doom" (`12:59`), exiting early out of fear rather than a systematic signal.
4. **Survivorship in Trending Metas**:
   * Winning streaks during Phase 1 relied on low-cap bonding curve runners during an active market session where copycat tokens consistently hit $\$30\text{k}\text{--}\$70\text{k}$ market caps. In low-volume regimes, a majority of these tokens rug/dump directly to 0 without offering take-profit liquidity.
