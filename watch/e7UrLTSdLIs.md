# Watched: https://www.youtube.com/watch?v=e7UrLTSdLIs

model `gemini-3.6-flash` · tokens in 165700 out 2593

Here is a detailed, skeptical breakdown and analysis of the video provided.

---

### 1. What's On Screen (Visual Details Missed by Audio)

* **01:21** — Initial Polymarket account portfolio balance: **$100.00 Cash / $100.00 Portfolio**.
* **03:18** — Kreo Telegram bot sample copy task screen shows a top trader with 30-day P&L of **+$1,716,569.83** using a fixed **10 USDC** order size.
* **04:25 - 05:00** — Chart timeframe shown on Polymarket: **5-Minute resolution** ("BTC 5 Minute Up or Down", e.g., 10:25–10:30 PM ET). The chart features a dashed horizontal **Target Line** representing the underlying index price at the start of the 5-minute window.
* **05:55 - 06:49** — **Manual Trade #1**:
  * **Entry**: $10 bet on "Up" at 85¢ odds (Avg entry 84.6¢).
  * **Mid-trade drawdowns shown on screen**:
    * 06:13: Value drops to $6.82 (-31.61%).
    * 06:18: Value drops to $3.97 (-59.77%).
  * **Exit**: Price spikes above target line at final second. Sold for **$11.34** (Realized P&L: **+$1.37 / +13.79%**). Portfolio Cash: **$101.34**.
* **07:07 - 07:53** — **Manual Trade #2**:
  * **Entry**: $5 bet on "Up" at 16¢–18¢ odds (3 mins remaining).
  * **Exit**: Sold at **$11.34** (Realized P&L: **+$6.24 / +125%**). Portfolio Cash: **$110.63**.
* **08:20 - 08:44** — **Manual Trade #3**:
  * **Entry**: $30 bet on "Down" at 64¢–65¢ odds.
  * **Mid-trade drawdown**: Price jumps above target line (-53.85%, -$15.90).
  * **Exit**: Panic cut for **$9.61** return (-$20.39 loss). Cash balance drops to **$89.23**.
* **09:16 - 09:35** — **Manual Trade #4**:
  * **Entry**: $20 bet on "Down" at 52¢ odds.
  * **Outcome**: Price rises above target. Position value drops to $0.41 (-97.92% loss).
* **09:55 - 10:28** — **Manual Trade #5**:
  * **Entry**: $19 (all-in) on "Up" at 21¢ odds.
  * **Outcome**: Total loss (-95.24%). Remaining account balance: **$3.34 total ($0.20 cash)**.
* **12:05 - 13:16** — **Polymarket Leaderboard & Wallet Selection**:
  * Filtered by: **Today** -> **Crypto**.
  * Wallet 1: `bigbraininvestor` (Joined Oct 2025, 496 views, $60.1K position value, Past Day P&L: **+$12,229.04**).
  * Wallet 2: `ponymarketsucks` (Joined Mar 2026, 1.7K views, 658 predictions, Past Day P&L: **+$10,099.94**, address: `0x42861b...816dba` / `0xEc5C5FA45889Ed...`).
* **14:09 - 17:40** — **Exact Copy-Trade Filter Panel Settings in Kreo Bot**:
  * **Step 1/9 (Target)**: `0x42861b...816dba`
  * **Step 2/9 (Task Name)**: `DIDDY`
  * **Step 3/9 (Buy Method)**: **Fixed** ($1.50 USDC per trade)
  * **Step 4/9 (Max Spend Limits)**: **$30.00** limit applied to **Whole Market**
  * **Step 5/9 (Slippage)**: **Custom** -> **7%**
  * **Step 6/9 (Odds Filter)**: **Skip** (No min/max odds filter)
  * **Step 7/9 (Stop Loss)**: **Off** (Skip)
  * **Step 8/9 (Take Profit)**: **Off** (Skip)
  * **Step 9/9 (Trade Behavior)**: **Buys + Sells**
  * **Monitoring Mode**: **Normal Mode** (copies once confirmed on-chain)
* **18:41 - 19:45** — **AI Match Panel Settings**:
  * Risk: Conservative | Category: Crypto | Style: Safe & Steady | Hold Time: Quick Flips | Activity: Full-Time | Priority: Strategy.
* **21:51** — **Copy-Trade Test #1 Mid-point P&L**: **+$80.68** on 45 trades ($66.27 invested).
* **23:01 - 23:33** — **Copy-Trade Test #1 Final P&L**: Available Balance: **$192.13** (Total P&L: **+$94.49**).
* **24:44 - 26:22** — **Kreo Web Chart Terminal**:
  * Real-time line chart with built-in quick execution buttons ($1, $5, $10, $20, $50).
  * Manual trades on terminal result in continuous losses, reducing balance back to **$172.17**.
* **28:06 - 28:46** — **Copy-Trade Test #2 Final Results**:
  * Open Positions Panel: Portfolio Value: $34.38, Available Balance: **$554.99**, PNL: **+$449.28**.
  * Task PnL Summary (28:46): Task Name: DIDDY | Total PnL: **+$531.06** | Amount of Trades: **192** | Invested Amount: **+$283.87**.
  * Polymarket Web Profile PnL Screenshot (28:22): **+$450.06 All Time** (`0xEc5C5FA45889Ed...`).

---

### 2. Concrete Trading Rules & Bot Testability

| Rule Type | Description / Parameters | Timestamp | Automated Testability |
| :--- | :--- | :--- | :--- |
| **Market Selection** | Trade 5-minute BTC "Up or Down" binary prediction contracts on Polymarket. | 04:25 | **Yes** (Standard API market stream) |
| **Manual Odds Strategy (Failed)** | Enter trades when odds are around 30¢ (offering ~3x return) with 3–4 minutes remaining in the 5-min window. | 07:11 | **Yes** (Order book odds & duration filtering) |
| **Copy-Trade Target Selection** | Select leaderboard wallets under "Today -> Crypto" with moderate daily volume (<$100k preferred) and high recency of trades (1–5 mins ago) to avoid high-volume automated market making bots. | 11:37 - 12:45 | **Partly** (Requires custom web/API scraping of Polymarket leaderboard & transaction history) |
| **Copy-Trade Order Sizing** | Fixed order sizing of **$1.50 USDC** per trade copied. | 15:50 | **Yes** |
| **Copy-Trade Max Budget** | Maximum cap of **$30.00 USDC** total exposure per single market/contract. | 16:18 | **Yes** |
| **Copy-Trade Execution Parameters** | **7% Slippage**, copy both **Buys & Sells**, **No Stop Loss**, **No Take Profit**, execution on **Normal Mode** (on-chain confirmation). | 16:37 - 17:35 | **Yes** |

---

### 3. Evidence Quality & Promotion Assessment

* **Proven on Screen**:
  * **Manual Trading Failure**: Screen capture clearly shows 5 consecutive manual trades resulting in near-total liquidation of the initial $100 balance ($100 $\rightarrow$ $3.34).
  * **Bot Interface Functionality**: The Kreo Telegram bot menu, order setup parameters, slippage inputs, and task configuration flow are demonstrated in real time.
* **Unproven / Unverified Claims**:
  * **Off-camera Gains**: The creator claims to have made "$3 off-camera" between manual trades.
  * **Unverified Copy Results**: While Telegram bot output cards and a Polymarket profile screenshot showing +$450.06 / +$531.06 P&L are displayed, the video relies heavily on time-lapses where the creator steps away from the room. On-chain transaction logs verifying that the $1.50 USDC copied orders matched the leader's exact fills without latency/slippage decay were not individually audited line-by-time on Etherscan/Polygonscan.
* **Sponsorships & Links**:
  * **Direct Sponsorship/Promotional Video**: The video explicitly advertises and promotes the **Kreo Polymarket Telegram Bot** (`kreo.trade/@setuh`), complete with referral links in the video description.

---

### 4. Contradictions & Logic Flaws

1. **AI Match Preference Selection vs. Narration**:
   * At **19:07**, the narrator explicitly says: *"If you're a real man, we're going to be clicking on these bottom three: Value Hunter, Momentum, and Contrarians."*
   * However, on screen at **18:55**, the option selected under "What trading style?" is **Safe & Steady**.
2. **Copy Trading vs. Manual Trading Discrepancy**:
   * The narrator claims manual trading is impossible due to "professional bots and insiders," yet attributes all copy-trading success to blindly following a single public wallet (`ponymarketsucks`) found on a public daily leaderboard. If public leaderboard traders are easily copyable with 7% slippage and $1.50 fixed sizing on 5-minute binary options, order fill latency and front-running would realistically impact returns in high-frequency scenarios (192 trades in ~30–60 mins).
3. **Risk Management Rhetoric**:
   * The creator mocks the concept of using Stop Loss or Take Profit options at **16:54** (*"We are grown men, we do not use a stop loss... hold everything to zero"*), which directly caused the 100% loss of the manual trading account in the first half of the video.
