# Watched: https://www.youtube.com/watch?v=DLKXgumP-Lo

model `gemini-3.6-flash` · tokens in 65764 out 1499

Here are structured markdown notes detailing the visual data, trading mechanics, evidence quality, and contradictions from the video.

---

### 1. What’s On Screen (Visual & Technical Details)

* **00:00–00:04**: Axiom terminal showing Solana token/meme coin listings across categories ("New Pairs", "Final Stretch", "Migrated") displaying market caps, liquidity, and pair ages.
* **00:05–01:36**: Tradovate interface displaying the **1-minute (`1m`) chart** for **Gold Futures (`GCZ5`)**. 
  * **Account Balance**: Initial Equity displayed as **$50,099.52 USD** (Open P/L: `$0.00`).
  * **00:46**: Brief cut to a prop-firm dashboard (Project X / Tradovate performance metric page) showing a $50,000 evaluation account with a $3,000 profit target ($53,000) and a $2,000 maximum drawdown threshold ($48,000 level).
* **02:28–02:37**: Navigating Tradovate chart settings (`Chart Type`, `Grid`, `Price Levels`, `Color Scheme`).
* **03:18**: Market Execution Order: `Buy 1 GCZ5 MKT - Filled - Fill 1@3988.5`.
* **03:21–03:28**: Live P&L position status bar: `-1@3988.5` showing live floating loss dropping from `-$50.00 USD` down to `-$140.00 USD`.
* **03:50**: Google Search bar visible on browser tab: `how to set a stop loss tradovate`.
* **04:26–04:30**: Fibonacci Retracement overlay applied to 1m chart showing default ratio lines (`0.0%`, `23.6%`, `38.2%`, `50.0%`, `61.8%`, `100.0%`).
* **05:08**: System audio alert: `"Order Filled"`. Position closed via stop out. Account Equity shown updated to **$49,534.42 USD** (~$565 loss).
* **05:18–05:46**: Navigation through Tradovate interface modules trying to locate order history logs/reports (`Trade Detail`, `Orders`, `Performance Center`).
* **06:02**: Screen shows a YouTube video titled `"Tradovate Tutorial | How To Enter & Exit Trades"` playing in a browser tab.
* **06:54**: Second Execution: `Sell 1 GCZ5 MKT - Filled - Fill 1@3991.4` (Short 1 contract at 3991.4).
* **08:20**: Audio alert: `"Stop Filled"`. Short trade stopped out. Account Equity drops to **$49,423.92 USD**.
* **08:44–09:07**: Third Execution: Long 1 contract (`GCZ5`) `@3993.0`, P&L showing floating profit around `+$220.00 USD`.
* **09:08–11:03**: Time-lapse sequence (1000x to 2000x speed) showing price consolidating sideways around 3997–4001.
* **11:03–11:10**: Take-profit order executes (`"Order Filled"`). Final Equity balance updated to **$50,088.32 USD**.

---

### 2. Concrete Trading Rules

| Rule Type | Parameter / Value | Timestamp | Automatable / Bot Checkable? |
| :--- | :--- | :--- | :--- |
| **Asset** | Gold Futures (`GCZ5` Dec 2025 Contract) | 00:05 | **Yes** |
| **Chart Timeframe** | 1-Minute (`1m`) | 00:05 | **Yes** |
| **Position Sizing** | 1 Contract per market order | 03:18 | **Yes** |
| **Entry Rule** | None (Discretionary/Guessing; "coin flip") | 03:11, 04:16 | **No** (No systematic criteria) |
| **Exit Rule (Stop Loss)** | Manual stop or trailing stop set arbitrarily | 03:40, 06:14 | **Partly** (Discretionary placement) |
| **Exit Rule (Take Profit)** | Manual target set arbitrarily above resistance | 04:20, 09:03 | **Partly** (Discretionary placement) |

---

### 3. Evidence Quality

* **Real/Simulated Account Data**: Trades were executed live on screen within Tradovate on a $50K funded evaluation account. Execution banners (`Filled`), audio prompts, and live account equity adjustments were visibly captured.
* **Track Record / Full History**: Not provided. Only 3 specific trades were filmed across the video session.
* **Promotional Content / Affiliations**: Mentions evaluation/funded account platforms (Project X, Tradovate), but no referral links or promotional codes are embedded in the video frames.

---

### 4. Contradictions & Inconsistencies

1. **Ease of Trading**:
   * *Claim* (01:20): *"I'm here to prove to you guys this shit is easy."*
   * *Contradiction* (01:21): On-screen text immediately reads: *"it was NOT EASY / not even the slightest bit easy....."*
2. **Self-Reliance vs. Searching Tutorials**:
   * *Claim* (06:21): *"Figured that shit out all by ourselves... didn't even need to look that shit up."*
   * *Contradiction* (03:50 & 06:02): Screen captures show him Googling *"how to set a stop loss tradovate"* and watching a YouTube tutorial on entering/exiting trades in Tradovate.
3. **Technical Analysis Jargon vs. Strategy**:
   * *Claim* (02:54): Cites technical terms like *"equilibrium liquidity grab, liquidity sweep, fair value gap, Fibonacci"*.
   * *Contradiction* (03:04, 04:16): Immediately admits: *"I have zero idea what the fuck I'm talking about... just look at a chart and flip a coin."*
