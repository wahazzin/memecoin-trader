# Watched: https://www.youtube.com/watch?v=2AH3BaacJ5s

model `gemini-3.7-flash` · tokens in 59315 out 1457

### 1. What's on Screen (Visual Details & Interface Setup)

* **Trading Platform & Dashboard**: The trader uses the **Axiom** trading terminal (`axiom.trade`) monitoring Solana memecoins on Pump.fun and LaunchLab/Bonk.
* **Layout Structure (00:00, 06:06, 10:08)**:
  * **Left/Center Columns**: "New Pairs", "Final Stretch" (bonding curve >70–80%), and "Migrated" (tokens that bonded to Raydium/DEX).
  * **Top Bar (00:13)**: Initial wallet balance displayed: `1.131 SOL` (~$150 USD). Target challenge: turn 1 SOL into multi-SOL.
  * **Right Side**: Live activity feed showing wallet tracker alerts, top traders, and token migrations.
* **Chart & Order Interface**:
  * **Timeframes**: Sub-minute charts (1-second, 5-second, and 15-second tick candles) on TradingView embed within Axiom.
  * **Buy Presets**: Quick-buy buttons configured at `0.1`, `0.2`, `0.5`, `1.0`, `P1`, `P2`, `P3`, `MAX`.
  * **Sell Presets**: `25%`, `50%`, `75%`, `100% (Full Clip)`.
  * **Bubble Maps / Holder Breakdown (02:56, 03:49, 07:08)**: Scans top holder distribution percentages, developer holding percentage, and cluster/bundle connections.

---

### 2. Concrete Trading Rules & Mechanics

| Timestamp | Rule Category | Parameters & Conditions | Bot Programmable? |
| :--- | :--- | :--- | :--- |
| **00:13 - 00:28** | **Position Sizing** | Allocate 1.0 SOL per trade ("full port"), leaving 0.1–0.13 SOL in reserve exclusively for Solana network priority transaction gas fees. | **Yes** |
| **01:19 - 01:45** | **Livestream Sentiment Entry** | Enter bonding tokens on Pump.fun if creator is live-streaming unique real-world content (e.g., painting live) with an active chat; enter at ~$70k–$76k Market Cap (MC). | **Partly** (requires live-stream status API; content assessment is subjective) |
| **02:44 - 02:47** | **Emergency Stop-Loss (Rug/Dump)** | If a large bundled sell occurs or price breaks below entry structure, execute a 100% market dump (`Full Clip`) to salvage remaining SOL (~50% loss cut). | **Yes** |
| **03:00 - 03:15** | **Community / Narrative Entry** | Buy tokens with distinct "cult" or viral X/Twitter branding at $11k–$15k MC, targeting an exit between $30k–$50k MC. | **Partly** (MC levels programmable; viral narrative requires LLM/social scraper) |
| **04:26 - 04:30** | **Rotation Exit** | Sell 100% of an open winning position immediately when spotting an early, fast-moving high-momentum runner on LaunchLab. | **Yes** |
| **05:13 - 05:50** | **Order-Book Tape Spoofing / Micro-Bidding** | Spam micro-buys ($0.01 / 0.0001 SOL) repeatedly during sideways/pullback consolidation to paint green candle ticks and make the feed appear actively bought. | **Yes** (automated transaction spamming script) |
| **07:40 - 08:08** | **Dev Dump / Top Holder Dip Entry** | Monitor top 10 holders; when a suspected developer/whale holding ~5–7% sells completely and price drops, buy the immediate bottom tick anticipating a bounce. | **Yes** |
| **09:18 - 09:24** | **Partial Take-Profit Scaling** | On a ~2x price expansion (from ~$11k MC to ~$21k–$23k MC), sell 50% of the bag at first resistance, followed by remaining 50% on exhaustion. | **Yes** |

---

### 3. Evidence Quality & Verifiability

* **P&L Proof vs. Off-Screen Gaps**:
  * **Trades 1 to 4**: Fully recorded live on chart with entry/exit execution bubbles and balance updates.
  * **Intermission Gap (06:07–06:27)**: Two trades (+0.6 SOL win and instant rug loss) were executed completely off-screen without video capture. The viewer only sees the balance adjusted to `1.39 SOL`.
  * **Trades 5 to 8**: Live on-screen entries/exits shown. Final balance reaches `2.457 SOL` at 10:08.
* **Wallet Addresses**: Specific public wallet keys are not explicitly displayed on screen, but individual transaction hashes and token contract addresses (CA) are visible in the platform search bars and community X links.
* **Sponsorships / Conflicts**: The video prominently displays the Axiom platform interface throughout, though no explicit affiliate referral pitch is delivered in the audio.

---

### 4. Contradictions & Critical Observations

* **Platform Manipulation Tactic (05:13–05:59)**: The trader explicitly demonstrates and advocates spamming 1-cent buys to game the charting engine into rendering full green candles on sub-minute views. While effective at creating visual urgency for retail retail-feed scrollers, this relies on market deception rather than technical or fundamental edge.
* **Risk Management Contradiction**: The trader starts with a strict "full port" strategy (allocating 100% of capital to a single illiquid micro-cap), which contradicts standard mathematical risk management and ruin-probability theory. A single un-sellable honeypot/rug would terminate the entire account.
* **Narrative Rationalization**: In Trade 1 (01:36–02:20), the trader claims the creator "could not have bundled" based purely on visual sympathy from the livestream, only to immediately get dumped on by early bundled wallets, demonstrating the unreliability of visual heuristics over on-chain bubble-map analysis.
