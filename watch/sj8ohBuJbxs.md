# Watched: https://www.youtube.com/watch?v=sj8ohBuJbxs

model `gemini-3.5-flash` · tokens in 162765 out 1889

Here is a detailed, skeptical analysis of the video's visual data, concrete rules, and evidence quality.

---

### 1. Screen vs. Narration (Visual Details Missed by the Transcript)

*   **Padre Terminal UI (00:04):** The platform shown is `trade.padre.gg/trenches`. The interface is divided into three columns: **New**, **Soon**, and **Migrated**. 
    *   Each token card displays: Ticker, Name, Age (e.g., `11m`), Market Cap (MC), Volume, Liquidity, Holders, and a "Bundled" percentage (e.g., `PEACHES` shows `10%` bundled, `$434K` MC, `1.4K` holders).
*   **Kolscan Leaderboard (04:38):** The leaderboard displays top traders on Solana. 
    *   **Cented** (Wallet: `CyaE1VxvBrahnPwKqm9VsdOryS2oMht2UFrKJHga54o`) is shown with:
        *   *Daily P&L:* $+153.81\text{ Sol}$ ($13,202.70) with a win rate of $106/10$.
        *   *Weekly P&L (04:45):* $+1,459.80\text{ Sol}$ ($125,309.00) with a win rate of $845/138$.
        *   *Monthly P&L (04:48):* $+5,701.07\text{ Sol}$ ($489,380.10) with a win rate of $3576/178$.
*   **JSON Wallet Import Structure (05:58):** The raw text file used to mass-import wallets into Padre Terminal contains structured JSON objects:
    ```json
    {
      "trackedWalletAddress": "62N1K57D37AUDG...",
      "name": "set",
      "emoji": "🦹",
      "alertsOnToast": true,
      "alertsOnBubble": true,
      "alertsOnFeed": true,
      "groups": ["Main"],
      "sound": "default"
    }
    ```
*   **Malibu/SOL Chart Analysis (07:46):** 
    *   **Timeframe:** $1\text{m}$ (indicated by "Malibu/SOL, 1m, Padre" in the top-left corner).
    *   **Visual Indicators:** No standard technical indicators (like EMAs or RSI) are used. Instead, the chart is overlaid with circular bubble icons representing tracked wallet transactions. Green bubbles represent buys, red bubbles represent sells. Badges labeled **DS** (Developer Sell) and **DB** (Developer Buy) are displayed on the chart.
    *   **Fast Wallet Profile (08:16):** Clicking on the trader "decu" opens a profile showing a highly volatile, spikey green line chart of realized P&L, along with tabs for "Most Profitable", "Active Positions", and "Dev Tokens".
*   **oilcoin/SOL Metrics (14:21):**
    *   **Eyeball Icon (Active Viewers):** Located in the top-left header. It shows "95" (hover text: "Users recently on this page").
    *   **Holders Tab (14:31):** Shows "Holders (306)". This visualizes the $90:300$ ($30\%$) viewer-to-holder ratio discussed by the narrator.
    *   **Meteora AMM V2 Warning (16:07):** A yellow circular icon next to the token name indicates it is on Meteora. The platform warns that these are often "scam tokens."
*   **DexScreener Banner Check (20:13):** The banner for `oilcoin` on DexScreener shows distinct black borders on the left and right sides of the text logo `"oilcoin"`, indicating the image aspect ratio was not properly formatted for a banner.

---

### 2. Concrete Trading Rules

| Rule Type | Description | Exact Numbers / Thresholds | Timestamp | Bot Checkable? |
| :--- | :--- | :--- | :--- | :--- |
| **Filter** | **KOL Wallet Concentration:** Avoid any token if multiple tracked KOL wallets enter early. | $\ge 2\text{ to } 3$ tracked wallets entering under $\$10\text{K}$ Market Cap. | 09:04 | **Yes** (If the bot has access to a database of tracked KOL addresses). |
| **Filter** | **Active Viewer Ratio:** Avoid tokens where the ratio of active page viewers to total holders is too low, indicating automated bundling/multi-walleting. | $\le 30\%$ of total holders are actively viewing the page. | 14:39 | **Yes** (If platform APIs expose active viewer metrics). |
| **Filter** | **Narrative Rerun Check:** Avoid tokens with tickers that have graduated to Raydium/Meteora multiple times. | Ticker has graduated $\ge 2$ times in the past. | 15:53 | **Yes** (Via historical graduation queries). |
| **Filter** | **Twitter Community Verification:** Community must have a contract address (CA) in the description, a pinned thesis post, and active moderation. | $3/3$ green lights on community checks. | 17:43 | **Partly** (Requires scraping and NLP to detect spam/drainer links). |
| **Filter** | **DexScreener Banner Check:** Avoid tokens where the DexScreener banner has black borders, indicating a lazy, automated launch tool. | Presence of black borders on the DexScreener banner. | 20:20 | **No** (Requires visual image analysis). |
| **Filter** | **Community Post Engagement:** Posts in the Twitter community must maintain a minimum level of views and likes to prove organic activity. | Posts $> 5\text{ minutes}$ old must have $\ge 100\text{ views}$ and $\ge 10\text{ likes}$. | 22:13 | **Yes** (Via Twitter/X API). |

---

### 3. Evidence Quality

*   **What is Proven on Screen:**
    *   The functionality and UI of Padre Terminal, DexScreener, and Kolscan.
    *   The existence of automated "vamp" tokens and multi-wallet bundles (demonstrated via transaction bubbles and historical graduation lists).
    *   The presence of unmoderated spam (wallet drainers) in dead Twitter communities.
*   **What is Only Claimed:**
    *   The profitability of these filtering rules. No backtest, systematic data, or long-term P&L statements are provided to prove that avoiding "Diddy" wallets or "bordered banners" results in a positive expected value ($EV$).
*   **Sponsorship / Referrals:**
    *   The video is a direct promotion for **Padre Terminal** ("Terminal"). At 08:28, the narrator explicitly directs viewers to sign up using "the first link in the description."

---

### 4. Contradictions and Weaknesses

*   **The Copy-Trading Contradiction:** The narrator strongly warns against copy trading ("*I recommend nobody ever copy trade... I promise you it is going to do you dirty*," 02:39). However, the core strategy of the video relies on scraping the top 100 wallets from Kolscan, importing them into a terminal, and using their entry points as the primary filter for whether a token is safe to buy. This is functionally manual copy-trading/shadow-trading.
*   **Subjective Banner Rule:** The "DexScreener banner border check" (20:20) is highly subjective. A legitimate, non-scam developer could easily upload a poorly formatted image, while a sophisticated scammer/bundler can easily format a banner perfectly to bypass this check.
*   **Platform-Specific Viewer Bias:** The "Active Viewer Ratio" (14:39) assumes that Padre Terminal's active viewer count represents the entire market's attention. It ignores users viewing the token on Photon, BullX, DexScreener, Birdeye, or Telegram trading bots, making the $30\%$ threshold mathematically unreliable.
