# Watched: https://www.youtube.com/watch?v=NR-ApzUzRBU

model `gemini-3.7-flash` · tokens in 69401 out 2078

Here are the detailed, skeptical markdown notes evaluating the trading system, rules, and evidence presented in the video.

---

### 1. What’s on Screen (Visual Details Missing from Audio)

* **Platform UI**: BullX / Hyper Vision terminal on Solana (DEX aggregator & meme coin sniper terminal) with side-by-side columns: *New Creations*, *About to Graduate*, and *Graduated*.
* **Filter Configuration Panel** (`01:03`–`01:13`):
  * **Target Column**: `About to Graduate`
  * `Insider wallets supply`: Max **30%** (Min left empty)
  * `Sniper wallets`: Empty
  * `Bot users`: Min **10** (Max left empty)
  * `Market Cap`: Min **$10,000** (Max left empty)
  * `Token Age (mins)`: Max **30** (Min left empty)
  * `Dev holding %`, `Liquidity`, `Volume`, `Txns`, `Buys`, `Sells`, `B.Curve %`: All left blank in the filter modal.
* **Token Analysis Views**:
  * `04:06`–`04:18`: Token badge inspection on *greed3*: Shows icons for Top Holders (`24%`), Dev Sold (`DS 2%`), Snipers (`1%`), Insider/Bot (`4%`), and Previous Deployer Migrations crown icon (`11`).
  * `04:48`–`05:48`: Holder Tab UI showing individual wallet holdings (`Remaining %`): Rank 1 = 3.5%, Rank 2 = 2.93%, Rank 3 = 2.69%, Top 10 = `22.86%`–`23.48%`. Identifies trade platforms via icons next to maker addresses (BullX icon, Trojan icon, Telegram bot icon).
  * `06:03`–`06:55`: **TrenchRadar Scanner** (Telegram bot interface):
    * Scans contract address for `$007DOG`.
    * Output displays: `Total Bundles: 11 (Holding) / 15 (Total)`, `Total SOL Spent: 34.74 SOL`, `Current Held Percentage: 17.5004%`, `Bonded: No`, `Creator Risk Profile - Total Created: 9`.
  * `07:20`–`08:26`: Pump.fun page view:
    * Sort comments setting: `Sort: time (DESC)`.
    * Bottom section: `Similar coins` module showing duplicate deployer history and recycled token images/names.
  * `08:50`–`09:56`: Trade Execution Chart on `$https` (HTTPS):
    * Chart view uses sub-minute candles (tick/second data with buy/sell bubble overlays).
    * Buy markers `B` and Sell markers `S` visible on chart. Entry around ~$15k–$20k mcap, exit at 2x peak.
  * `11:28`–`11:49`: Chart on `$egg` showing high-volume spike to $30k followed by immediate vertical red candle dump to near-zero upon specific caller wallet exits.

---

### 2. Concrete Trading Rules & Automation Feasibility

| Category | Rule / Metric | Exact Values / Conditions | Timestamp | Bot Checkable? |
| :--- | :--- | :--- | :--- | :--- |
| **Screener Filter** | Column Selection | Focus solely on `About to Graduate` (tokens approaching bonding curve completion). | `01:03`, `03:20` | **Yes** (Pump.fun bonding curve threshold ~70–95%) |
| **Screener Filter** | Market Cap | Minimum **$10,000**. | `01:06`, `01:52` | **Yes** |
| **Screener Filter** | Token Age | Maximum **30 minutes**. Reject tokens older than 30 min that have not migrated. | `01:09`, `02:11` | **Yes** |
| **Screener Filter** | Bot Users | Minimum **10** (and >50% of total active volume/holders via trading bots). | `01:05`, `01:45` | **Partly** (Depends on DEX API tracking bot maker tags) |
| **Screener Filter** | Insider Supply | Maximum **30%** insider wallet holdings (target 20%–30% range). | `01:11`, `01:18` | **Yes** (Via bundle scanner/token metadata) |
| **Safety / Rug Filter** | Dev Holdings | Dev holding must be **0%**; reject if Dev holds any remaining supply (even 2%). | `04:05` | **Yes** |
| **Safety / Rug Filter** | Deployer History | Reject if deployer has high migration count with rapid dumps. | `04:15` | **Yes** |
| **Safety / Rug Filter** | Bundle Concentration | Reject low-cap tokens (<$50k mcap) if bundled supply is **>5%** (disqualifies 17%+ bundles). For >$100k mcap, max **10%**. | `06:12`, `07:01` | **Yes** (Via TrenchRadar / bundle APIs) |
| **Safety / Rug Filter** | Top Holder Limits | Individual top holders (excluding bonding curve) must each hold **≤3.5%**. | `04:59` | **Yes** |
| **Safety / Rug Filter** | Token Originality | Check Pump.fun "Similar coins"; reject direct clones/re-deploys within short window. | `08:12` | **Partly** (Image hashing / name matching required) |
| **Caller / Smart Wallet Filter** | Specific Wallet Blacklist | Blacklist toxic caller wallets (e.g., "Cupsy", "Waddles") that trigger instant dumps. Whitelist conviction holders (e.g., "Inferno", "Ghosty", "Dartmouth"). | `08:38`, `09:18`, `11:38` | **Yes** (Tracking on-chain wallet addresses) |
| **Price Action / Entry** | Breakout Structure | Series of higher highs, shallow pullbacks bought back rapidly, breaking previous ATHs with genuine multi-wallet volume. | `10:47`–`11:26` | **Yes** (Technical indicators: swing highs/lows + depth of retracement) |
| **Exit Strategy** | Take Profit Target | Fixed take-profit at **2x (100% gain)** from entry price. | `09:21`, `10:09` | **Yes** |

---

### 3. Evidence Quality & Promotion Assessment

* **Proof of Execution**:
  * The creator shows chart overlays with buy (`B`) and sell (`S`) markers on `$https` indicating an actual trade entry and a 2x exit.
  * **Missing Data**: No full wallet address, full transaction hashes, or verified P&L ledger / cumulative statement is provided. Individual win shown, but overall win rate/net profitability across all trades is not documented.
* **Backtesting & Sample Size**: 
  * Only isolated, cherry-picked examples are shown (1 successful trade on `$https`, 1 failed bundle example on `$007DOG`, 1 scam deployer on `greed3`, 1 caller dump on `$egg`). No statistical sample or automated backtest results.
* **Commercial / Promotional Tie-ins**:
  * Active promotion of creator's Twitch live-streaming channel at `12:22`–`12:35`.
  * External tool mentions (BullX, TrenchRadar Scanner).

---

### 4. Contradictions & Critical Observations

1. **Holding vs. Flipping Narrative**:
   * The video title and intro claim to teach "How to spot 100x meme coins," but throughout the video, the creator explicitly states: *"We're not holding shit to 100x... I'm only really in it for a 2x"* (`09:25`, `10:07`). The actual strategy is a micro-scalp (2x flip), contradicting the 100x premise.
2. **"Bot Users" Definition**:
   * The narrator claims "Bot users" means "real people using Telegram trading bots (BullX, Photon, Trojan) rather than automated bots" (`01:30`–`01:45`), arguing that >50% bot users proves organic interest. In reality, high "bot user" volume on micro-cap bonding curves is frequently automated wash trading and sniper scripts designed to simulate organic activity.
3. **Subjective "Pump.fun Comments" Rule**:
   * The presenter advises verifying if comments say "it's OG, clean, no bundles, bullish" (`07:58`), while acknowledging that most comments are bot spam. Filtering for genuine human sentiment using pump.fun comment sections is easily manipulated by automated shilling bots.
