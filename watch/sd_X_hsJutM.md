# Watched: https://www.youtube.com/watch?v=sd_X_hsJutM

model `gemini-3.6-flash` · tokens in 133648 out 2417

Here is the detailed analysis of the **Memecoin Blueprint Day 2** video, covering on-screen data, explicit trading/filter rules, evidence quality, and potential red flags.

---

### 1. What's on Screen (Visual & Panel Breakdown)

* **Platform UI:** Padre Terminal (`trade.padre.gg/trenches`).
* **[03:01 - 03:14] Trenches ("New Pairs") Filter Panel:**
  * **$ Metrics -> Market Cap (Min):** `$6,000`
  * **Token Age (mins) (Max):** `6`
* **[03:48 - 04:21] "Soon" (Pump.fun Final Stretch / Bonding Curve Graduation) Filter Panel:**
  * **Token Age (mins) (Max):** `30`
  * **Vitals -> Pro Holders (Min):** `20`
  * **$ Metrics -> Market Cap (Min):** `$8,500`
* **[04:28 - 04:46] "Migrated" Filter Panel:**
  * **Vitals -> Pro Holders (Min):** `100`
  * **$ Metrics -> Market Cap (Min):** `$30,000`
* **[05:14 - 06:36] Solana Presets (Trade Fee Configuration) Panel (Preset 1 / P1):**
  * **Buy Settings:**
    * Priority Fee (`Prio`): `0.0001 SOL`
    * Jito/Tip (`Tip`): `0.001 SOL`
    * Slippage: `20%`
    * MEV Protection: **OFF** (Toggle disabled)
  * **Sell Settings:**
    * Priority Fee (`Prio`): `0.0001 SOL`
    * Jito/Tip (`Tip`): `0.001 SOL`
    * Slippage: `50%`
    * MEV Protection: **OFF** (Toggle disabled)
* **[09:42 - 20:10] Holder & Security Inspection Tabs:**
  * **Holders Tab Columns:** Rank, Address, SOL Balance, Bought (Avg MC), Sold (Avg MC), PNL, Hold For, Remaining %.
  * **[10:34] Graphic Example (Bundled Distribution):** Shows top wallets holding identical percentages (`1.1%`, `1.1%`, `1.1%`, `1.1%`).
  * **[11:22] Graphic Example (SOL Balance Bundle):** Shows wallets with near-identical low SOL balances (`0.175`, `0.102`, `0.145`, `0.007`, `0.282`).
  * **[11:42 - 12:04] "Funded By" Tab & Graphic Example:** Shows wallet funding sources (Exchange / Bridge names, time elapsed). Graphic highlights multiple top wallets funded by `Binance` at the exact same time (`4d • 2d`).
  * **[13:09] Graphic Example (Trading Platform):** Top holders all displaying identical platform/bot icons.
  * **[14:00 - 15:05] Wallet Trade History Pop-up:** Displays wallet metrics (Realized PnL, Win Rate) and individual token trade logs (`ECSTASY`, `FIX`, `fropie`, `RETRO`, `ARIA`).
  * **[16:11 - 18:36] Bubble Maps Visualizer:** Nodes representing wallets; lines/arrows showing supply transfers between wallets. Graphic at `18:25` shows dense circular web clusters. Text warning at `18:35`: *"If a Bubblemap is 'too clean' then that is bad as well"* (due to mixing services).
  * **[19:19 - 19:42] Fresh Wallet ("Leaf") Indicator:** Green leaf icon on Padre indicates a wallet that had 0 SOL until recently. Graphic at `19:42` shows top holders filled with green leaf icons.
* **[20:30 - 21:50] External Discord Security Bot ("Qutex" / `ca-analysis` channel):**
  * Automated contract address (CA) check returning: **Rug Score** (e.g., `1/100`), **Security Status** (`SAFE - Low risk detected`), **Market Data** (MC, LP, FDV, Holders, Price), **Liquidity Info** (LP Locked), and **Warnings** summary.

---

### 2. Concrete Rules & Bot Checkability

| Timestamp | Category | Rule Description | Parameter / Threshold | Bot Checkable? |
| :--- | :--- | :--- | :--- | :--- |
| **03:08** | Filter | **Trenches Minimum Market Cap** | Min Market Cap = `$6,000` | **Yes** |
| **03:13** | Filter | **Trenches Maximum Token Age** | Max Age = `6 minutes` | **Yes** |
| **04:08** | Filter | **"Soon" Column Maximum Token Age** | Max Age = `30 minutes` | **Yes** |
| **04:12** | Filter | **"Soon" Column Minimum Pro Holders** | Min Pro Holders = `20` | **Yes** |
| **04:17** | Filter | **"Soon" Column Minimum Market Cap** | Min Market Cap = `$8,500` | **Yes** |
| **04:33** | Filter | **"Migrated" Column Minimum Pro Holders** | Min Pro Holders = `100` | **Yes** |
| **04:38** | Filter | **"Migrated" Column Minimum Market Cap** | Min Market Cap = `$30,000` | **Yes** |
| **05:44** | Fee / Execution | **Buy Priority Fee** | Set Priority Fee to `0.0001 SOL` | **Yes** |
| **05:56** | Fee / Execution | **Buy Jito / Tip Fee** | Set Tip Fee to `0.001 SOL` | **Yes** |
| **06:07** | Fee / Execution | **Buy Slippage Tolerance** | Set Slippage to `20%` | **Yes** |
| **05:59** | Fee / Execution | **Buy MEV Protection** | Turn MEV Protection **OFF** | **Yes** |
| **06:27** | Fee / Execution | **Sell Slippage Tolerance** | Set Slippage to `50%` | **Yes** |
| **10:01** | Risk / Filter | **Top Holder Supply Cap** | Reject token if **any single holder** (excluding Liquidity Pool) holds `> 4%` of total supply | **Yes** |
| **10:34** | Risk / Filter | **Identical Distribution Check** | Reject token if multiple top holders own near-identical % of supply (e.g., 5+ wallets holding ~1.1% or ~2.5% each) | **Yes** |
| **11:13** | Risk / Filter | **SOL Balance Symmetry** | Reject token if top holders maintain nearly identical SOL balances | **Yes** |
| **11:56** | Risk / Filter | **CEX Funding Clustering** | Reject token if top holders were funded by the same exchange/bridge at the same timestamp | **Yes** |
| **13:09** | Risk / Filter | **Platform Uniformity** | Red flag if top holders share the exact same rare trading terminal/bot | **Yes** |
| **14:48** | Risk / Filter | **Overlapping Trade History** | Reject token if top holders share identical recent buy/sell history across obscure prior tokens | **Yes** |
| **18:25** | Risk / Filter | **Bubblemap Cluster Size** | Reject token if connected wallet clusters hold `> 5-6%` aggregate supply or exhibit dense multi-wallet web visual patterns | **Partly** (Visual cluster algorithms required) |
| **19:42** | Risk / Filter | **Fresh Wallet Density** | Reject token if top holders are predominantly fresh wallets (green leaf / created within minutes) making large buys | **Yes** |

---

### 3. Evidence Quality & Promotion

* **Proven vs. Claimed:**
  * **Proven on screen:** The mechanics of setting up filters, instant trade presets, inspecting holder lists, viewing funding sources, reading bubble maps, and running a contract through Discord security bots (`Qutex`).
  * **Claimed without backtest/data:** Claims that following these checks will make a trader profitable or prevent 99% of losses. No verified long-term PnL statement or system backtest log is provided in this episode.
* **Sponsorships & Referrals:**
  * **Padre Terminal (`trade.padre.gg`):** Heavily promoted throughout the video with affiliate links in the description (`23:38`).
  * **Gated Discord Group ("PF Trenches"):** Promoted as free, but requires holding $50 in a wallet or completing an "Elite Upgrade" verification to unlock automated scanning tools (`20:45`).

---

### 4. Contradictions & Risk Red Flags

1. **MEV Protection Disabled on High Slippage (50%):**
   * *Contradiction:* The presenter explicitly instructs users to turn MEV Protection **OFF** while setting Sell Slippage to **50%** (`06:23`, `06:27`). In fast-moving Solana memecoin markets, disabling MEV protection while allowing 50% slippage exposes transactions to sandwich attacks and front-running by MEV bots, which contradicts the stated goal of saving money on fees/execution.
2. **"Too Clean" vs. "Clustered" Bubble Map Dilemma:**
   * *Red Flag:* The video states that heavily clustered bubble maps indicate bad developer bundles (`18:25`), but then notes that a bubble map that is "too clean" (no connections) is *also* bad because developers use coin mixers to mask connections (`18:35`). This creates a subjective, non-falsifiable heuristic where both connected and unconnected visuals can be interpreted as fraudulent.
3. **Manual Inspection Speed Bottleneck:**
   * *Execution Risk:* Performing all 7 manual inspections (Holder %, SOL Balances, Funded By, Platform Type, Trade History Overlap, Bubble Maps, Fresh Wallets) on tokens under 6 minutes old is visually demonstrated on single coins, but practically impossible to execute manually before price action completes in fast-moving memecoin launches without automated RPC tooling.
