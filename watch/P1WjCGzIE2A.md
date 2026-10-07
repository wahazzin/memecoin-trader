# Watched: https://www.youtube.com/watch?v=P1WjCGzIE2A

model `gemini-3.8-flash` · tokens in 142655 out 2761

### 1. What's on Screen (Visual Details Missed by Audio)

* **Trading Platform & Layout (00:00–04:30):** The presenter operates on **Axiom Trade** (`axiom.trade/pulse?chain=sol`). The interface divides tokens into three primary pipeline columns: `New Pairs`, `Final Stretch` (bonding curve progress nearing migration), and `Migrated`.
* **P&L Screenshots (00:47–00:51):**
  * Displays two graphic performance cards:
    * *"February 2025: +77.1 SOL, PNL +98%, Start Balance 78.88, End Balance 156"*.
    * *"+160.3 SOL, PNL +100%, Start Balance 160.3, End Balance 320.6"*.
  * Both graphics feature a referral code promo: `axiom.trade/?ref=setuh` (*"Save 10% off fees"*).
  * Shows a monthly calendar heatmap (+77.15 SOL / +$15.6K) with green daily boxes (e.g., `+0.052`, `+1.92`, `+3.106`, `+5.205`).
  * **Critical observation:** No public Solana wallet addresses, transaction hashes, or raw ledger links are displayed. All proof consists of cropped UI cards.
* **Axiom Terminal Filter Setup (04:28–06:53):**
  * **Protocols/Launchpads:** `Unselect All` clicked, only **Pump** (`pump.fun`) selected across all columns (04:33, 05:08). Excludes Raydium, Meteora AMM, Bonk, Moonshot, Heaven, Candle, etc.
  * **New Pairs Filter Form (05:46–05:55):**
    * Age: `Min [blank]`, `Max [5]` `m` (minutes).
    * Metrics: Market Cap `Min [7000]` USD.
  * **Final Stretch Filter Form (06:27–06:53):**
    * Audit tab: Age Max `40` `m` (ensuring dropdown is set to `m`, not `s` or `h`).
    * Dev Holding %: Max `5`.
    * Insiders %: Max `20`.
    * Pro Traders: Min `10`.
    * Metrics tab: Market Cap Min `8000` USD.
  * **Discord Preset Reference Card (07:10):**
    * Summary card shows slightly altered numbers:
      * *New Pairs:* Age Max 3 mins, Dev Holding Max 9%, Market Cap Min 7000.
      * *Final Stretch:* Age Max 40, Dev Holding Max 5, Snipers Max 40, Insiders Max 30, Pro Traders Min 10, Market Cap Min 8000.
      * *Migrated:* Holders Min 50, Top 10 Max 50, Market Cap Min 20000.
* **Holder & Funding Inspection Panel (09:22–11:15):**
  * Columns shown: `Wallet`, `SOL Balance (Last Active)`, `Bought (Avg Buy)`, `Sold (Avg Sell)`, `U. PnL % / $`, `Remaining`, `Funding`.
  * **Clean token:** Top holders have diverse SOL balances (e.g., 5.56 SOL, 3.31 SOL, 1.67 SOL, 4.77 SOL) and disparate funding creation dates (`6d`, `22d`, `3y`, `7mo`, `2d`).
  * **Bundled/Scam token (10:04, 11:13):** Top holders have repetitive/identical balances (`0.1 SOL`, `0.1 SOL`, `0.02 SOL`) and identical funding timestamps from centralized exchanges (e.g., all funded via Coinbase `14d ago` or `1h ago`).
* **Chart Interface & Timeframes (18:37–21:22):**
  * Chart asset: `FINN (Middle Finger)` pair `FINN/USD on Pump V1`.
  * Chart timeframe: Axiom chart toggled between `1s` and `1m`.
  * Indicators: Native Axiom Market Cap overlay (`marketCap/Price`), volume histogram, bubble map overlay.

---

### 2. Concrete Rules Table

| Rule Type | Exact Parameter / Threshold | Timestamp | Bot Testable? | Notes / Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Launchpad Filter** | Protocol = `Pump` (Pump.fun) only | 04:33 | **Yes** | Discard all other DEXs/launchpads (Raydium, Meteora, etc.). |
| **New Pairs Filter** | Market Cap $\ge \$7,000$, Age $\le 3\text{--}5\text{ min}$, Dev $\le 9\%$ | 05:52, 07:10 | **Yes** | Filters out dead zero-volume launches. |
| **Final Stretch Filter** | Market Cap $\ge \$8,000$, Age $\le 40\text{ min}$, Dev $\le 5\%$, Insiders $\le 20\text{--}30\%$, Pro Traders $\ge 10$, Snipers $\le 40\%$ | 06:27–06:53, 07:10 | **Yes** | Applied to near-bonding curve tokens. |
| **Pipeline Selection** | Only trade `New Pairs` or bottom 4 tokens of `Final Stretch` | 18:22–18:36 | **Yes** | Avoids the top 2 tokens in Final Stretch (too saturated). |
| **Category Filter** | Token metadata must be flagged as "Community Token" (two-people icon) | 07:34–08:23 | **Yes** | Rejects "Tweet" (feather icon) and "Profile" (single person icon) tokens. |
| **Anti-Bundle Check 1** | Top 5 holders must NOT have uniform SOL balances (e.g., all 0.1 SOL) | 09:37–10:14 | **Yes** | Programmatically check standard deviation of Top 5 balances. |
| **Anti-Bundle Check 2** | Top 5 holder funding timestamps/sources must NOT be identical | 10:30–11:15 | **Yes** | Rejects tokens where wallets share identical funding age/source. |
| **Anti-Bundle Check 3** | Reject chart pattern showing a vertical single green spike from launch ($5k to $10k+) without organic trades | 14:00–15:20 | **Yes** | Detects dev single-block multi-buys. |
| **Social Filter 1** | CA (Contract Address) must be present in X Community Bio/Description | 12:08 | **Partly** | Requires X API / scraping. |
| **Social Filter 2** | Pinned post in X Community must contain the CA | 12:21 | **Partly** | Requires X API / scraping. |
| **Social Filter 3** | X Community feed must have active organic discussion (no link spam) | 12:35 | **No** | Subjective / NLP classification needed. |
| **Dip Entry Rule** | Buy upon a **40% to 50% retracement** from a local All-Time High | 19:05–19:16, 20:10–21:15 | **Yes** | Explicitly prohibits buying small 10% pullbacks. |
| **Stop Loss Rule** | Hard exit immediately if price drops below average entry price | 19:38–19:50 | **Yes** | Break-even / negative PnL market sell trigger. |
| **Take Profit Target** | Target 40% to 50% rebound (or $2\times$ bounce) off the dip level | 20:06–21:22, 22:07 | **Yes** | Measured rebound back toward previous highs. |
| **Position Sizing (0.1 SOL port)** | New Pairs: 0.05 SOL; Final Stretch: 0.07 SOL max | 21:54–21:58 | **Yes** | Allocates 50% to 70% of total bankroll per trade. |
| **Position Sizing (0.5 SOL port)** | New Pairs: 0.1 SOL; Final Stretch: 0.2 SOL max | 22:14–22:18 | **Yes** | Allocates 20% to 40% of total bankroll per trade. |
| **Position Sizing (1.0 SOL port)** | New Pairs: 0.25 SOL; Final Stretch: 0.4 SOL max | 22:34–22:38 | **Yes** | Allocates 25% to 40% of total bankroll per trade. |
| **Position Sizing (5.0 SOL port)** | New Pairs: 1.0 SOL; Final Stretch: 1.5 SOL max | 22:57–23:01 | **Yes** | Allocates 20% to 30% of total bankroll per trade. |
| **Account Threshold** | Portfolios $< 0.1$ SOL are barred from trading | 23:20–23:56 | **Yes** | Gas fees and DEX swap fees prevent profitability below this level. |

---

### 3. Evidence Quality

* **Claimed vs. Proven:**
  * **Claimed:** Consistently making $10,000–$15,000/month for 8 consecutive months without losing days, turning 0.1 SOL into 100 SOL.
  * **Proven:** Zero verified live trades executed during the video. All analysis is retrospective on selected historical charts (`FINN`, `BIBLE`). P&L graphics are static, cropped images without on-chain wallet verification.
* **Commercial Interests:**
  * Presenter heavily promotes their Axiom referral link (`axiom.trade/?ref=setuh`) across overlays and cards.
  * Funnels viewers into a Discord community (`discord.gg/...`).

---

### 4. Contradictions & Execution Realities

* **Stop Loss vs. Slippage/Gas Mechanics:**
  * The presenter advises: *"As soon as that shit drops below your average price, you need to be selling"* (19:38). On Solana memecoins, each round-trip transaction incurs a 1% DEX fee, priority gas fees (often 0.005–0.01 SOL), and slippage/price impact (commonly 2%–10%). A strict 0% price stop guarantees an immediate realized loss of 5%–15% on execution friction alone. High market volatility will prematurely stop out almost every entry immediately after fill.
* **Filter Parameter Inconsistencies:**
  * In the video screencast (06:43), the presenter enters `20%` for Max Insiders in Final Stretch; the Discord preset card shown at 07:10 specifies `MAX 30`.
  * New Pairs Max Age is set to `5m` on screen (05:49), but the Discord card lists `MAX 3 MINS` (07:10).
* **Extreme Risk of Ruin in Sizing:**
  * The recommended bet sizing for a 0.1 SOL account is 0.07 SOL (70% of total bankroll on a single trade), and for a 1.0 SOL account, 0.40 SOL (40% of bankroll). In memecoin markets where tokens frequently suffer liquidity pulls or 90%+ flash dumps, risking 40%–70% of equity per trade violates fundamental capital preservation principles.
