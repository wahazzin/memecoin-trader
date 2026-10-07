# Watched: https://www.youtube.com/watch?v=u_4pIrZFlUc

model `gemini-3.6-flash` · tokens in 47945 out 1547

Here is an analytical breakdown of the trading session shown in the video, evaluating the on-screen data, trading mechanics, evidence quality, and execution risks.

---

### 1. What’s On Screen (UI, Charts & P&L Analysis)

The video shows live trading on **Axiom Pro**, a specialized trading terminal for Solana DEX/memecoin trading (pump.fun / LaunchLab / Raydium tokens).

* **Wallet Balance & P&L Progression**:
  * **00:07**: Verified starting balance on screen: **2.434 SOL** (up from 1.0 SOL in Episode 1).
  * **01:16**: P&L card for token `ez`: **+1.216 SOL (+150%)**, Invested: `0.81 SOL`. Handle: `@Setuh`.
  * **06:20**: P&L card for token `CIRCLE`: **+0.616 SOL (+60.5%)**, Invested: `1.018 SOL`.
  * **08:19**: Verified ending balance on screen: **5.161 SOL** (Net session gain: **+2.727 SOL**).
  * *Note*: Full wallet public keys are cropped out of the top header; only live numeric balances and the Twitter handle `@Setuh` are visible.

* **Interface Elements & Settings**:
  * **Chart Timeframes**: Preset bar options visible on chart headers (`1s`, `5s`, `1m`, `5m`, `15m`, `1h`). Primary execution view uses **1-minute (1m)** candles with fast tick-level updates.
  * **Execution UI**: Axiom Pro panel featuring one-click pre-set sizing buttons (`0.1`, `0.2`, `0.5`, `1.0 SOL`) and quick sell percentage clips (`10%`, `25%`, `50%`, `100% / Full Clip`).
  * **On-Chart Indicators**: Visual transaction mapping overlay displaying green dots (buy fills) and red dots (sell fills) mapped directly onto price candles.
  * **04:34**: External browser check showing Twitter/X community panel (`somethingcoin` community hub).
  * **08:02**: Axiom search panel showing token clone detection (`DOGWATER` deployed 50+ times in a single day).

---

### 2. Concrete Trading Rules & Bot Testability

| Rule Type | Description & Exact Numbers | Timestamp | Bot Testable? |
| :--- | :--- | :--- | :--- |
| **Position Sizing** | Risk 0.5 to 1.0 SOL (~20–30% of current total wallet) per trade setup. | 00:36, 06:20 | **Partly** (Sizing percentage is scriptable, token selection is discretionary) |
| **Partial Scale-Out** | Take 50% profit at ~1.5x–2.0x gain or $15k–$25k Market Cap (MC) threshold; leave 10–20% "moonbag". | 00:40, 00:54 | **Yes** (Automated limit/scaling targets) |
| **Wallet Copy / Bottom Signal** | Monitor specific tracked wallets on-chain. Hold through drawdowns if tracked "bottom signal" wallets buy the dip. | 02:12 | **Yes** (On-chain wallet monitoring trigger) |
| **Contract / Spam Filter** | Search token name; if token contract has been re-launched >5 times in 24 hours, execute full exit ("full clip"). | 08:02 | **Yes** (API query for contract creation count) |
| **Dev Concentration Exit** | Cut position immediately if top holder / dev wallet holds >5% or executes heavy dumps. | 03:22, 04:31 | **Yes** (Automated token holder threshold filter) |
| **Full Liquidation** | Sell 100% position immediately if upward momentum breaks or MEV slippage distorts entry. | 03:02, 06:31 | **Yes** (Trailing stop / loss threshold) |

---

### 3. Evidence Quality & Transparency

* **Proven On Screen**:
  * **Sequential P&L**: The live wallet balance changes in real-time across the session (**2.434 SOL $\rightarrow$ 5.161 SOL**).
  * **Loss Inclusion**: Unfiltered reporting of multiple losing trades: `-0.2 SOL` on `IRS` (03:04), `-0.3 SOL` on `SASK` rug (03:38), `-0.4 SOL` on `somethingcoin` (04:46).
  * **Execution Fills**: Visual transaction dots (green/red) and system popup confirmation toasts verify active execution on Raydium/pump.fun bonding curves.

* **Claimed / Unproven**:
  * **04:52 (`MERDOCK`) & 07:02 (`GROK`)**: Buys were not recorded live on video; only retrospective chart analysis and final P&L adjustments were shown.
  * **07:15**: The claim that he "fumbled 8 SOL in potential profit" on `GROK` is purely speculative hindsight bias based on a peak chart wick.

* **Monetization & Affiliations**:
  * Axiom Pro referral prompt displayed on exported P&L cards (*"Save 10% of fees"*).

---

### 4. Strategy Contradictions & Execution Risks

1. **Stated Goals vs. Execution Reality**:
   * **Contradiction**: The trader explicitly states he is hunting for *"3x, 4x, 5x multis"* (06:49). However, due to fear from prior losses, he repeatedly panic-sells or "full clips" positions after minor +10–30% pops or accidental misclicks (06:31: *"my finger slipped, didn't mean to full clip"*).

2. **High-Slippage & MEV Exposure**:
   * At **02:02**, the trader attempts to ape into `CATGIRL` at a $330k MC and gets MEV-sandwiched down to an entry of $270k MC, instantly putting the position in severe drawdown. Automated systems in this ecosystem require private RPC endpoints and tip fees to prevent front-running.

3. **Extreme Adverse Selection (Rug-Pull Meta)**:
   * More than half of the traded tokens in this session were bundled insider rugs or instant dumps (`SASK`, `somethingcoin`, `CIRCLE`). Trading ultra-low MC Solana tokens (<$10k MC) manually carries a negative expected value ($EV$) unless strict automated on-chain security filters (holder distribution, mint authority, freeze authority) are enforced prior to block inclusion.
