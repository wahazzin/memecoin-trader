# Watched: https://www.youtube.com/watch?v=vYyOchs9P_g

model `gemini-3.7-flash` · tokens in 157236 out 2332

### 1. What’s on Screen (Visual Details Transcript Misses)

* **Initial Claims & Wallet Screen (00:04, 01:43):**
  * 00:04: Mobile Phantom wallet overlay showing `$14.90` (`0.10281 SOL`).
  * 01:43: Mobile wallet screenshot titled `"MAIN JIN"` showing `$87.87` (`0.478965 SOL`).
* **P&L Screenshots (00:41, 00:46, 00:53):**
  * 00:41: AxiomPro graphic showing `MAX Realized +$42.3K`, Total Bought `$975K`, Total Sold `$1.02M`, Referral `@setuh`. Cropped marketing card; no wallet address, transaction IDs, or verifiable on-chain history.
  * 00:46: Nova Trade graphic reading `"April 2025 +$13.77K"`, Bought `$213.21K`, Sold `$226.99K`, ROI `+6.46%`. (Note the graphic shows a future/fictional date "April 2025").
  * 00:53: AxiomPro card showing `MAX Realized 2 wallets +$72.4K`.
* **Platform & Workspace (02:00–28:45):**
  * Web trading terminal: `nova.trade` using the **Cosmo** dashboard (columns: *Newly Created*, *About to Graduate*, *Graduated*).
  * Chart timeframe: 1-second (`1s`) tick chart (`PEPUM/USD on PumpFun Nova - 1s`, `RETARDIO`, `HEALCOIN`, `SMURFCAT`).
* **Filter Setup Panels (05:00–07:44):**
  * **Newly Created Filter Panel (05:20–06:43):**
    * *Dex:* Only `PumpFun` enabled (all others unselected: Raydium, LaunchLab, Moonshot, etc.).
    * *General Tab:* Market Cap Min = `$7,000` (Max = blank).
    * *Audit Tab:* Age (mins) Max = `5` (Min = blank).
  * **About to Graduate Filter Panel (07:05–07:43):**
    * *Dex:* Only `PumpFun` enabled.
    * *General Tab:* Market Cap Min = `$8,000`.
    * *Audit Tab:* Age (mins) Max = `80`, Dev Hold (%) Max = `5%`, Insiders Holder (%) Max = `20%`.
* **Order Execution Settings (08:26–10:05):**
  * **Buy Tab:** Slippage = `35%`, MEV Protect = `OFF`, Auto-Tip = `OFF`, Priority Fee = `0.001 SOL`, Buy Tip = `0.001 SOL`.
  * **Sell Tab:** Slippage = `70%`, MEV Protect = `OFF`, Auto-Tip = `OFF`, Priority Fee = `0.001 SOL`, Sell Tip = `0.001 SOL`.
* **Holders / Funding Audit View (11:47–12:50, 24:45):**
  * Inspecting table columns: `% Owned`, `Balance`, `Remaining`, `Funding`.
  * 12:45: On-screen example of bundled tokens showing multiple top holders funded identically (`FixedFloat 3h • 0.98 SOL`, `Coinbase 49m • 3.51 SOL`).
* **Ignite Feature Screen (27:23–27:48):**
  * Algorithmic alert feed displaying token tickers, current MC, and retrospective peak multipliers (e.g., `6.14x -> 7.13 SOL`, `4.08x -> 3.07 SOL`).

---

### 2. Concrete Trading Rules & Automation Feasibility

| Rule / Parameter | Exact Value / Condition | Timestamp | Bot Testable? | Notes / Logic |
| :--- | :--- | :--- | :--- | :--- |
| **DEX Routing Filter** | Only trade tokens on `PumpFun` | 05:20, 07:08 | **Yes** | Exclude tokens from Raydium, Moonshot, etc. |
| **New Pairs Filter (Scan 1)** | Market Cap $\ge \$7,000$; Token Age $\le 5\text{ mins}$ | 06:14–06:33 | **Yes** | Query token creation timestamp and pool liquidity/MC. |
| **Graduation Filter (Scan 2)** | Market Cap $\ge \$8,000$; Token Age $\le 80\text{ mins}$; Dev Hold $\le 5\%$; Insider Hold $\le 20\%$ | 07:11–07:43 | **Yes** | Parse audit metadata fields from API. |
| **Top Holder Distribution Cap** | Top 3 to 5 individual holders must each hold $< 4\%$ of total supply | 11:58–12:09 | **Yes** | Calculate `max(holder_pct)` for the top 5 non-bonding-curve wallets. |
| **Funding Wallet Bundle Check** | Discard if top holders share identical funding transaction source/timestamp/amount | 12:40–12:55 | **Yes** | Trace first funding transaction of top 10 wallets. Reject if shared cluster detected. |
| **Dev Sell Prerequisite** | Dev wallet must have sold its initial allocation (`Dev Sell` event logged) | 24:33–24:40 | **Yes** | Check if the deployer wallet balance is $0$ or has executed a sell transaction. |
| **Original vs. Derivative Check** | Ticker/name must not be a direct derivative/re-launch of past runners; no prior duplicate on PumpFun | 19:10–20:30 | **Partly** | String distance/fuzzy matching against historical tokens can automate most of this; visual meme check requires vision model or manual review. |
| **Social / Community Gate** | Active Twitter community with recent posts within last 5–10 mins; Dex profile paid | 13:14–13:56 | **Partly** | API check for paid DEX metadata; scraping Twitter for engagement frequency. |
| **Entry Price Condition** | Market Cap between $\$20,000$ and $\$40,000$, executing on a $30\%–40\%$ pullback from local high | 16:15–16:55 | **Yes** | `current_MC between 20k and 40k AND current_MC <= peak_MC * 0.70`. |
| **Execution Slippage & Fees** | Buy: 35% slippage, 0.001 SOL priority, 0.001 SOL tip; Sell: 70% slippage, 0.001 SOL priority, 0.001 SOL tip | 09:34–10:04 | **Yes** | Hardcoded RPC transaction parameters. |
| **Take-Profit Target** | Scalp targets at $2\text{x}$ to $3\text{x}$ ($+100\%$ to $+200\%$) gain | 14:52–14:55 | **Yes** | Limit order / TP trigger based on entry price. |
| **Copy-Trading Prohibition** | Do NOT auto-buy when tracked wallets buy; only use tracker as a warning/exit flag | 26:37–27:12 | **Yes** | Blacklist copy-buy triggers. |

---

### 3. Evidence Quality

* **Proof Quality:** Low. All P&L records shown (00:41, 00:46, 00:53) are cropped promotional graphical cards without visible transaction hashes, wallet public keys, or full unedited ledger histories. One graphic (00:46) shows the date `"April 2025"` (a future date relative to standard production).
* **Live Trading Proof:** None. The presenter walks through historical and static 1-second charts (`PEPUM`, `RETARDIO`, `HEALCOIN`, `SMURFCAT`), annotating past swings in hindsight without executing live orders on stream.
* **Commercial Interests:**
  * Heavy affiliate promotion for the `nova.trade` platform with referral links (`@setuh`) offering fee cashbacks (03:54, 28:38).
  * Promotion of a personal Discord group (26:18) to download wallet tracker configuration files.

---

### 4. Contradictions & Execution Realities

* **Slippage vs. Low Capital Scaling:**
  * The video claims trading with very low capital ($0.1$ SOL / ~$15) can turn into $100,000. However, paying $0.001$ SOL priority fee $+ 0.001$ SOL tip on every buy and sell, combined with $35\%$ buy slippage and $70\%$ sell slippage, means a single round-trip trade can instantly lose $30\%–60\%$ of position equity on fee/slippage drag alone on a small $0.1$ SOL balance.
* **MEV Protection "Off" Recommendation:**
  * The presenter advises keeping MEV Protection **OFF** to avoid extra fees, claiming low-cap memecoins on PumpFun never get MEVed (08:37–08:48). In high-volatility Solana bonding curves, sandwich bots and frontrunners routinely extract value from transactions with $35\%–70\%$ slippage regardless of trade size.
* **Subjective Community Valuation vs. Algorithmic Trading:**
  * The narrator repeatedly emphasizes that one must "feel" the meme and verify "people are messing with it" (13:30–13:38), while simultaneously arguing that price action is purely mechanical and can be traded on 1-second charts (15:46–16:00).
