# Watched: https://www.youtube.com/watch?v=-GwaA1K11kA

model `gemini-3.6-flash` · tokens in 166777 out 2478

An analysis of the memecoin scalping strategy presented in the video, detailing visual terminal evidence, trade execution rules, P&L transparency, and underlying risks.

---

### 1. What's On Screen (Visual & Terminal Details)

The video displays live trading on the **Padre Terminal** (`trade.padre.gg`), targeting micro-cap Solana memecoins primarily launched via Pump.fun and Mayhem bonding curves.

* **Interface & Views**:
  * **Trenches Dashboard**: Grid view split into three columns: `New` (just created), `Soon` (nearing bonding completion), and `Migrated` (graduated to Raydium/DEXs).
  * **Trading Chart**: Displays 1-second and 1-minute candlestick charts with real-time execution markers (green `B` circles for buys, red `S` circles for sells).
  * **Order Panel**: Features quick-buy presets (`P1`, `P2`, `P3`) configured for instant execution (typically `0.25 SOL`, `0.5 SOL`, `1.0 SOL`).
  * **P&L Summary Panel**: Shows exact breakdown per token: `Invested`, `Sold`, `Remaining`, and `T. PNL` (Total Profit & Loss in SOL and percentage).
  * **Header Wallet Tracker**: Displays real-time total SOL balance in the wallet (e.g., `1.00 SOL` starting $\rightarrow$ `10.80 SOL` final).

* **Key P&L Milestones & Screenshots Shown On Screen**:
  * **02:20 - 02:59 (`JAMESON/SOL`)**: Invested `0.505 SOL`, Sold `1.637 SOL` $\rightarrow$ **+1.132 SOL (+224%)**. Wallet: `2.07 SOL`.
  * **05:25 (`Minimi/SOL`)**: Initial buy dumped by KOLs; re-bid dip. Invested `2.026 SOL`, Sold `2.792 SOL` $\rightarrow$ **+0.766 SOL**. Wallet: `2.75 SOL`.
  * **06:34 - 06:38 (`TOOL/SOL`)**: Invested `0.505 SOL`, Sold `1.245 SOL` $\rightarrow$ **+0.7405 SOL (+146.6%)**. Wallet: `3.48 SOL`.
  * **07:32 (`GTA6/SOL`)**: Invested `0.505 SOL`, Sold `1.158 SOL` $\rightarrow$ **+0.653 SOL**. Wallet: `4.09 SOL`.
  * **08:44 (`MCAT/SOL` - Mayhem Mode)**: Invested `1.012 SOL`, Sold `2.090 SOL` $\rightarrow$ **+1.078 SOL**. Wallet: `5.15 SOL`.
  * **10:22 (`KRABS/SOL`)**: Invested `0.515 SOL`, Sold `0.849 SOL` $\rightarrow$ **+0.334 SOL**. Wallet: `5.48 SOL`.
  * **12:03 (`Riona/SOL`)**: Dev claimed GitHub fees. Invested `1.010 SOL`, Sold `2.302 SOL` $\rightarrow$ **+1.292 SOL**. Wallet: `6.72 SOL`.
  * **13:14 - 13:34 (`JACKS/SOL`)**: Invested `0.508 SOL`, Sold `0.325 SOL` $\rightarrow$ **-0.183 SOL (-36%)**. Wallet: `6.53 SOL`.
  * **14:32 (`ok/SOL`)**: Invested `0.512 SOL`, Sold `1.107 SOL` $\rightarrow$ **+0.595 SOL**. Wallet: `7.11 SOL`.
  * **15:47 (`Father/SOL`)**: Invested `0.505 SOL`, Sold `1.134 SOL` $\rightarrow$ **+0.629 SOL**. Wallet: `7.72 SOL`.
  * **17:24 (`SHELL/SOL`)**: Invested `1.017 SOL`, Sold `1.415 SOL` $\rightarrow$ **+0.398 SOL**. Wallet: `8.10 SOL`.
  * **19:36 - 19:54 (`Scissors/SOL`)**: Invested `1.212 SOL`, Sold `0.312 SOL` $\rightarrow$ **-0.899 SOL (-74%)**. Wallet: `7.20 SOL`.
  * **20:55 (`TRADOOR/SOL`)**: Invested `0.505 SOL`, Sold `1.216 SOL` $\rightarrow$ **+0.7114 SOL (+140%)**. Wallet: `8.40 SOL`.
  * **21:57 (`DUMPSTER/SOL`)**: Invested `0.505 SOL`, Sold `1.005 SOL` $\rightarrow$ **+0.500 SOL**. Wallet: `8.90 SOL`.
  * **23:34 (`Jackson/SOL`)**: Invested `0.510 SOL`, Sold `1.207 SOL` $\rightarrow$ **+0.697 SOL**. Wallet: `9.12 SOL`.
  * **24:48 (`CLOUT/SOL`)**: Bundled/dumped by dev. Loss of **~0.36 SOL**. Wallet: `8.76 SOL`.
  * **26:02 (`STONE/SOL`)**: Invested `0.506 SOL`, Sold `1.213 SOL` $\rightarrow$ **+0.707 SOL**. Wallet: `9.46 SOL`.
  * **27:55 - 28:00 (`r/MSB/SOL`)**: Invested `0.505 SOL`, Sold `1.883 SOL` $\rightarrow$ **+1.378 SOL**. Wallet: **10.80 SOL** (~$1,000 equivalent).

---

### 2. Strategy Rules & Bot-Checkability

| Rule Type | Exact Parameter / Condition | Timestamp | Bot Checkable? |
| :--- | :--- | :--- | :--- |
| **Market Segment** | Focus exclusively on pre-graduation bonding curve tokens ("Trenches") between **$5k and $30k Market Cap** (MC). | 00:43 - 01:12 | **Yes** |
| **Position Sizing** | Start with **0.5 SOL** fixed size per trade on a 1.0 SOL portfolio (50% account risk). Scale to 0.7–1.2 SOL once portfolio exceeds 6.0 SOL. | 02:20, 19:13, 21:04 | **Yes** |
| **Narrative Filter** | Token must have active Twitter/X, Reddit, or Instagram social traction (e.g., viral memes, official company news, active GitHub dev). | 03:52, 05:55, 13:52 | **Partly** (via social APIs) |
| **Derivative Cap** | When trading derivative/spin-off coins, target **strictly a 2x return** (100% gain) and exit. Do not hold for 3x–4x due to rapid decay. | 22:13 - 22:35 | **Yes** |
| **Sniper/Bundle Filter**| If top launch holders/snipers hold a large percentage of supply without selling, treat as high-risk rug candidate; exit on weakness. | 18:47 - 19:10 | **Yes** (via holder distribution API) |
| **Time-Based Stop** | Exit position if token price/volume stagnates for **10 to 50 minutes** without establishing an upward trend. | 05:34, 13:16 | **Yes** |
| **Dip Re-Entry** | If a high-conviction viral narrative dumps due to early influencer/KOL sells, re-bid at the MC floor (~$20k) after heavy wallets exit. | 04:27 - 04:42 | **Partly** |
| **Profit Taking** | Scale out into momentum/spike candles; take full exit between **1.5x and 3x** profit targets. | 02:45, 06:46, 27:31 | **Yes** |

---

### 3. Evidence Quality

* **Proven on Screen**:
  * Live trade execution overlays directly on Padre charts (Buy `B` and Sell `S` markers correspond to timestamped price action).
  * Full transparency on losses: Shown in sequence with complete P&L tabs (`-0.183 SOL` on JACKS, `-0.899 SOL` on Scissors, `-0.36 SOL` on CLOUT).
  * Continuous wallet balance tracking in the terminal top header across 18 sequential trades.

* **Claimed vs. Unproven**:
  * **Wallet Address**: The full public key of the Solana wallet is not displayed (obscured under custom profile label `1 SOL VID`), preventing independent block-explorer verification of transaction signatures.
  * **Timeframe**: The video claims "24 Hours" in the thumbnail/title, but the creator verbally references sleeping overnight and completing the challenge over 2 days (approx. 48 hours).

* **Promotions & Incentives**:
  * Referral link to Padre Terminal (`trade.padre.gg/setuh`) promoted throughout the video.
  * Promotion of the creator's free Discord community (`PF Trenches`).

---

### 4. Technical Contradictions & Execution Risks

1. **High Account Concentration Risk**:
  * Sizing 0.5 SOL on a 1.0 SOL starting portfolio represents a **50% portfolio risk per trade**. A single 100% rug pull or 80% loss (such as the `Scissors/SOL` trade where 0.9 SOL was lost) early in the sequence would invalidate the challenge or liquidate half the capital.
2. **Liquidity Impact & Slippage**:
  * Selling 1.0–1.8 SOL out of microcaps with $5k–$15k Market Caps creates significant price impact. While terminal P&L cards reflect executed fill prices, manual traders copying this strategy face heavy slippage and MEV front-running on low-liquidity bonding curves.
3. **Subjective Narrative Evaluation**:
  * "Social virality" and "funny memes" are evaluated subjectively in real time. Because many microcaps rug-pull within seconds, non-automated subjective entries carry high failure rates during slow market conditions.
