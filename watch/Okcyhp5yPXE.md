# Watched: https://www.youtube.com/watch?v=Okcyhp5yPXE

model `gemini-3.7-flash` · tokens in 141492 out 2018

Here are the detailed, objective markdown notes analyzing the video, visual settings, trading logic, and evidence presented:

---

### 1. What's on Screen (Visual Details Missing from Audio)

- **Platform & Interface**:
  - Web interface is **Axiom Trade** (`axiom.trade/pulse`), a Solana memecoin screening and fast-execution terminal.
  - Layout features three primary scanner columns: **New Pairs**, **Final Stretch** (bonding curve near completion / pre-Raydium migration), and **Migrated** (bonded/migrated to Raydium/DEX).
  - Side panel tracks real-time global trades and tracked "Pro Traders" / "KOLs".
  - Charting is TradingView embedded within Axiom, set to **1-second (1s)** or **1-minute (1m)** candles.
- **Holder Analysis & Bubble Maps (03:45–06:10, 20:45–21:05)**:
  - **Holders Tab**: Displays wallet address, SOL balance, time active, amount bought/sold, average buy, PnL, % remaining, and funding source (e.g., Coinbase, Kraken, or specific wallet address).
  - **Bubblemap Panel (InsightX)**: Shows wallet clusters. Bundled tokens visually show a single central funding node distributing SOL in green radiating clusters to dozens of sub-wallets, or a uniform circle of identical-sized grey/colored bubbles.
- **DEX Paid Indicator (07:15–08:18)**:
  - Badges on token card indicating `Paid` DEX screener update status and timestamp relative to token age and market cap.
- **P&L Screenshots / Performance Proof**:
  - No verified wallet balance, total PnL statement, or trade log is shown.
  - Charts shown during KOL/tracked wallet dumps (e.g., "Cooker", "DV") are historical 1-second charts illustrating sudden sell-offs after pumps, but creator's execution entries/exits on these charts are not shown.

---

### 2. Concrete Rules & Settings

| Timestamp | Category | Rule / Metric | Exact Parameters | Bot Checkable? |
| :--- | :--- | :--- | :--- | :--- |
| **01:37** | **Filter** | Community vs. Tweet Meta | Prefer tokens with the "View community on X" icon (two blue user icons); avoid raw "tweet" tokens with single text/image posts. | **Yes** (Metadata / Social flags) |
| **03:45** | **Rug Check** | Top Holder SOL Balance | Reject token if multiple top holders share identical or nearly identical fractional SOL balances (e.g., multiple wallets with ~0.203–0.254 SOL). | **Yes** (Wallet analysis) |
| **04:28** | **Rug Check** | Wallet Creation / Funding Timing | Reject token if top 4+ wallets share the exact same funding age (e.g., all funded "1d" ago from the same parent address). | **Yes** (On-chain cluster analysis) |
| **05:15** | **Rug Check** | Bubblemap Cluster Check | Reject if Bubblemap (InsightX) shows a single funding wallet distributing tokens into multiple holding clusters, or a multi-wallet cluster >3%. | **Partly** (Requires visual/API graph clustering) |
| **07:30** | **Rug Check** | DEX Screener Pre-Payment | Reject if DEX Screener fee is paid while Market Cap is low ($15,000 – $30,000). Developer paying DEX fee early implies artificial bundling. | **Yes** (DEX paid status + Market Cap threshold) |
| **09:33** | **Scanner Filter** | **New Pairs Column** | - **Protocols**: `Pump`, `Heaven`<br>- **Audit Age**: Max `3 mins`<br>- **Dev Holding**: Max `10%`<br>- **Min Market Cap**: `$7,000` | **Yes** |
| **10:40** | **Scanner Filter** | **Final Stretch Column** | - **Protocols**: `Pump`<br>- **Audit Age**: Max `15 mins`<br>- **Dev Holding**: Max `5%`<br>- **Snipers**: Max `20%`<br>- **Insiders**: Max `20%`<br>- **Pro Traders**: Min `10`<br>- **Min Market Cap**: `$8,000` | **Yes** |
| **12:21** | **Scanner Filter** | **Migrated Column** | - **Protocols**: Select All<br>- **Min Holders**: `50`<br>- **Min Pro Traders**: `50`<br>- **Min Market Cap**: `$20,000` | **Yes** |
| **14:05** | **Verification** | OG / Copycat Detection | Search full token name (not ticker) across all launchpads. If misspelled or identical art exists from earlier tokens, reject. | **Partly** (Text matching / NLP, art requires perceptual hash) |
| **16:47** | **Exit Rule** | KOL / Tracked Wallet Entry | If a known KOL / high-volume tracked wallet (e.g., "DV", "Cupsey", "Cooker") buys in, **exit/sell immediately** to front-run their inevitable dump. | **Yes** (Watchlist address transaction monitoring) |
| **19:45** | **Rug Check** | False Low Top-10 Concentration | Reject if top 10 holder percentage is suspiciously low (e.g., exactly ~13%) while first candle is a single dev buy wicked to $10k MC. | **Yes** |
| **21:33** | **Execution** | **Preset 1 (Standard / 1–10 SOL)** | - **Buy Settings**:<br>  - Slippage: `35%`<br>  - Priority Fee: `0.001 SOL`<br>  - Bribe: `0.001 SOL`<br>  - MEV Mode: `Reduced`<br>- **Sell Settings**:<br>  - Slippage: `70%`<br>  - Priority Fee: `0.001 SOL`<br>  - Bribe: `0.01 SOL`<br>  - Max Fee: `0.1 SOL`<br>  - MEV Mode: `Reduced` | **Yes** |
| **24:00** | **Execution** | **Preset 2 (Micro Size / 0.1–0.5 SOL)** | - **Buy Settings**:<br>  - Slippage: `20%`<br>  - Priority Fee: `0.000001 SOL`<br>  - Bribe: `0.00000 SOL`<br>  - MEV Mode: `Off`<br>- **Sell Settings**:<br>  - Slippage: `20%`<br>  - Priority Fee: `0.000001 SOL`<br>  - Bribe: `0.00001 SOL`<br>  - MEV Mode: `Off` | **Yes** |

---

### 3. Evidence Quality

- **Claims vs. Proof**:
  - **Claimed**: The creator states they have ridden coins from $7k–$10k MC to millions of dollars multiple times.
  - **Proven**: No historical transaction ledger, verified PnL statement, or live trades are shown in this video. All chart demonstrations are post-mortem reviews on 1-second charts.
- **Sponsorship & Affiliation**:
  - The creator mentions their own Discord community and previous "1 SOL challenge" YouTube series.
  - Axiom interface is being promoted with specific platform-dependent features (Axiom Pro Traders, Lighthouse volume, InsightX Bubblemaps).

---

### 4. Contradictions & System Risks

1. **Tracked Wallets: Follow vs. Fade Inversion**:
   - Most retail traders track smart wallets to copy trade them. The presenter's explicit rule is the exact opposite: **use tracked wallets solely as an immediate sell trigger** because copy-trader volume creates artificial spikes followed by violent dumping.
2. **Slippage Discrepancy on Micro Accounts**:
   - For standard accounts, the presenter uses **70% sell slippage** to guarantee exit speed during high volatility. However, for micro accounts (<0.5 SOL), he sets sell slippage to **20%** to avoid fees, which directly contradicts the requirement of getting out instantly when a chart begins dumping. A 20% slippage on a fast-dumping memecoin will frequently fail transactions.
3. **"Too Clean" Metric Paradox**:
   - The presenter notes that both high top-holder concentration (>20%) AND suspiciously low top-holder concentration (~13% distributed across dozens of wallets created on the same day) indicate rugs. An automated bot must check internal wallet funding links rather than top-10 concentration percentages alone.
