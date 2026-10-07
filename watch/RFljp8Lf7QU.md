# Watched: https://www.youtube.com/watch?v=RFljp8Lf7QU

model `gemini-3.5-flash` · tokens in 144482 out 1467

Here are the markdown notes analyzing the trading video for your automated system development.

---

### 1. On-Screen Analysis (Visuals vs. Audio)

*   **Trading Platform & Interface (00:00 - 02:26):** 
    *   The platform shown is **Axiom Pro** (`axiom.trade/pulse/chain=sol`). 
    *   The dashboard displays three main columns: **New Pairs**, **Final Stretch**, and **Migrated**. 
    *   The right sidebar shows a real-time "Trades" feed with columns for Time, Name, Token, Amount (in SOL), and Market Cap (MC).
*   **Chart Settings & Timeframe (03:36 - 04:15):** 
    *   The chart shown is for `nichecoin/SOL` on **Pump v1** using an extremely noisy **1-second (1s) timeframe**.
    *   The "Token Info" panel on the right displays: *Top 10 Holders: 15.77%*, *Top 10 K: 0%*, *Holders: 1.22k*, and *Dev: 1.18%* (marked with a red warning icon).
    *   At **04:05**, the cursor demonstrates switching the P&L bar display from USD (`$`) to SOL (`Ξ`).
*   **Wallet Tracker Interface (11:59 - 13:06):**
    *   The left panel shows custom tracked wallets with metrics like "V $191K MC @ $49.7K".
    *   At **12:44**, the "Display Options" dropdown menu is opened, showing options to toggle: *Outliers, Migration, DEX Paid, My Trades, Dev Trades, Tracked Trades, KOL Trades, and X Mentions*.
    *   At **13:22**, the 1s chart displays a vertical cluster of green (buy) and red (sell) bubbles plotted directly on the price candles, showing exactly where tracked wallets executed trades.
*   **P&L Proof & Channel Promotion (25:47 - 25:52):**
    *   No live, unedited P&L statements, wallet addresses, or transaction histories are verified on screen. 
    *   The video ends by showing the creator's YouTube channel (`@setuhh`) with thumbnails claiming extreme, unproven results: *"I Tried Trading Memecoins For 2 Hours: $0.12 to $9,956.52"* and *"Turning $10 Into $500"*.

---

### 2. Concrete Trading Rules

| Rule Type | Rule Description | Timestamp | Bot Checkable? |
| :--- | :--- | :--- | :--- |
| **Filter** | **P&L Unit Filter:** Switch the trading terminal's P&L display from USD to SOL to remove fiat-denominated emotional bias. | 04:05 | **Yes** (Natively calculate all metrics in SOL/base token). |
| **Filter** | **Tracked Wallet Saturation:** Do not enter a coin if there are more than **2 tracked/KOL wallets** already holding or actively trading it. | 13:22 | **Yes** (Requires a database of tracked wallet addresses to query active token holders). |
| **Filter** | **Market Activity Filter:** If pair creation rate, volume, or volatility drops below baseline thresholds (or if scanning for "hours" yields no setups), halt trading. | 18:12 | **Yes** (Can be automated using rolling volume/volatility thresholds). |
| **Sizing / Exit** | **Daily Consecutive Loss Limit:** Stop trading for the day immediately after **5 consecutive losing trades**. | 19:51 | **Yes** (Simple counter on daily trade history). |
| **Sizing / Exit** | **Daily Consecutive Win Limit:** Stop trading for the day after **5 consecutive winning trades** once a ballpark profit target is met. | 23:01 | **Yes** (Simple counter on daily trade history). |
| **Targeting** | **Ballpark Profit Targets:** Set a rough, non-specific daily target range (e.g., aiming for ~2-4 SOL starting from 1 SOL) rather than a rigid decimal target to avoid over-trading. | 24:47 | **Yes** (Can be programmed as a soft target range). |

---

### 3. Evidence Quality

*   **What is Proven:** The video successfully demonstrates the UI features of Axiom Pro, specifically how to toggle display settings (USD to SOL) and how to overlay tracked wallet transactions onto a 1-second chart.
*   **What is Only Claimed:** The creator claims to have started trading with only $70 in his bank account and to have achieved a "100x position" within a year. No cryptographic proof (e.g., Solscan signatures, verified public portfolio tracking) is provided to back up these claims.
*   **Funnels & Referrals:** The creator heavily promotes a "completely free" Discord group in the description. These groups typically serve as marketing funnels for referral links (e.g., sign-up bonuses on trading terminals/bots) or future paid mentorships.

---

### 4. Internal Contradictions & Common Sense Flaws

*   **The Clickbait Contradiction:** The creator spends a significant portion of the video (06:30 - 11:35) warning viewers about the psychological dangers of comparing themselves to high-earning traders and chasing unrealistic gains. However, his own channel thumbnails (shown at 25:51) leverage extreme FOMO, claiming to turn **$0.12 into $9,956.52 in just 2 hours** (an mathematically absurd 8,297,100% return).
*   **The "Money is Gone" Paradox:** The creator advises traders to adopt the mindset that "as soon as money leaves your bank account, it is already gone/does not exist" (03:24). If a trader truly treats capital as completely lost play-money, setting strict rules to stop trading after 5 consecutive losses to "preserve capital" (19:51) is logically redundant.
*   **1-Second Timeframe Noise:** The video showcases strategies on a **1-second chart**. In live execution, 1s charts are dominated by MEV bot front-running, sandwich attacks, and extreme latency slippage. Attempting to manually or semi-systematically trade 1s charts based on visual "tracked wallet bubbles" is highly impractical due to execution delays.
