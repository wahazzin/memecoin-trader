# Watched: https://www.youtube.com/watch?v=fnIb5k8PBuM

model `gemini-3.6-flash` · tokens in 286166 out 2973

Here is a detailed, objective markdown analysis of the video.

---

# Memecoin Scalping Blueprint (Day 4) — Video Analysis & System Notes

---

## 1. What's on Screen (Visual & UI Details)

**Trading Platform:** Padre Terminal (`trade.padre.gg/trenches`).
**Blockchain / Exchange Context:** Solana (`SOL`), pump.fun bonding curves, and Raydium migrated pairs.

### Timestamps & Visual Breakdown

- **00:00 - 01:52**: Day 4 Introduction overlay screen. Shows Padre Trenches interface across New Pairs, Soon (Final Stretch), and Migrated (Raydium) columns.
- **01:53 - 04:20 | Step 1: Updated Filters (Trenches Settings)**
  - **New Pairs Filter Panel** (`03:26 - 03:38`):
    - `Metrics -> Market cap`: Min **$3,500** (`3500`).
  - **Soon (Final Stretch) Filter Panel** (`03:50 - 03:55`):
    - `Metrics -> Market cap`: Min **$6,000** (`6000`).
- **04:20 - 16:26 | Step 2: Scam Charts vs. Real Charts Identification**
  - **04:58 - 07:01**: *Scam Pattern #1 (The Dev/Bundle Trap)*
    - Visual: 1 huge green candle (dev buy + bundle), immediate thin red wick/candle (dev dump), second sharp green candle to 5K–6K Market Cap (MCAP), then spike to 10K MCAP, followed by instant drop to zero.
    - Live Chart Example (`07:02`): Token `GE-Sim 2.0/SOL`.
  - **07:39 - 09:21**: *Scam Pattern #2 (The Choppy Bundle Staircase)*
    - Visual: Single massive green candle (dev buy) taking market cap from 1K to ~10K MCAP, followed by micro-choppy, tight green/red "staircase" price action with no real pullbacks or organic dips.
    - Live Chart Example (`08:43`): Token `UNEMployed/SOL`.
  - **09:22 - 10:30**: *Scam Pattern #3 (Linear Staircase)*
    - Visual: Smooth, artificial diagonal line/staircase composed of uniform tiny candles rising steadily from 2K to 10K MCAP without sharp sell wicks.
    - Live Chart Example (`10:04`): Token `DRE/SOL`.
  - **11:08 - 14:40**: *Real Chart Pattern #1 (Organic Price Action)*
    - Visual: Varied candle sizes, distinct initial dev/sniper sell-off creating a clear floor/dip (around 3K–4K MCAP), followed by organic buyer recovery.
    - Live Chart Example (`12:51`): Token `DANGERSOL`.
  - **14:41 - 16:13**: *Real Chart Pattern #2 (Dev Bundle Hold)*
    - Visual: Dev buys with bundle, holds bag without instant dump; price experiences organic pullbacks and volume swings.
- **16:26 - 22:00 | Padre Terminal UI Customization Settings**
  - **Path:** Padre `Customize` button (top right) -> `Token` tab (`18:00 - 19:14`):
    - **$ Metrics Panel (`18:12`):**
      - `Size`: **Large**
      - `Stats digits`: **Short** / **Rounded**
      - `Volume`: **Checked**
      - `Total fees`: **Checked**
      - `Total txns`: **Unchecked**
      - `Market cap`: **Checked**
    - **Vitals Panel (`18:34`):**
      - `Total holders`: **Checked**
      - `Pro holders`: **Checked**
      - `Dev bonded`: **Unchecked**
      - `Dev created`: **Checked**
      - `Fresh wallet buys`: **Unchecked** *(Optional toggle mentioned)*
      - `Recent visitors`: **Checked** *(Highlighted as critical)*
      - `Market cap in stats`: **Unchecked**
    - **Audit Panel (`19:02`):**
      - `Value coloring`: **Bright**
      - `Top 10 holders`: **Checked**
      - `Dev holding`: **Checked**
      - `Dev funded`: **Checked**
      - `Snipers count`: **Unchecked**
      - `Snipers holding`: **Checked**
      - `Insiders holding`: **Checked**
      - `Bundles`: **Checked**
      - `Dex paid`: **Checked**
      - `Dex boosted`: **Checked**
      - `Dex paid timestamp`: **Checked**
  - **Spam Filtering Toggle (`21:36`):**
    - `Filters -> Vitals -> Holders`: Min = **1** (hides empty spam-deployer tokens).
- **22:00 - 31:26 | Step 3: Sniping / Scalping New Pairs**
  - **23:51 - 27:38**: Visual chart schematic for New Pair entry:
    - Initial launch at ~2K MCAP -> Pumps to 6K–8K MCAP via dev/bundles.
    - Sharp pullback/dump of 50%–60% down to 3K–4K MCAP floor (dev/bundle exit).
    - Live Chart Example (`26:25`): Token `PENNY/SOL` (pumps to 7K–8K MCAP, drops ~60% to 3K MCAP, rebounds to 10K+ MCAP).
- **31:26 - 46:17 | Step 4: Final Stretch (Soon) Scalping**
  - **38:37 - 42:30**: *40% Dip Method Setup:*
    - Diagram showing rise to 25K–30K MCAP, followed by a 40%–50% dip to ~15K MCAP, then a 2x–3x expansion.
    - Live Chart Example (`40:50`): Token `Gnome/SOL` (pumps to 16K, dips 43% to 9K MCAP, expands +176% to 26K MCAP).
  - **42:49 - 45:34**: *Tracked Dev Wallet Method Setup:*
    - Diagram showing launch, initial spike to 10K MCAP, then flat sideways consolidation/range at 10K MCAP before an upward breakout.
  - **45:34**: Visual highlight on Padre UI pointing to **"Dev Tokens (24h)"** history tab at the bottom of the execution pane.
- **46:17 - 51:07 | Final Step: Migrated / Graduated Scalping**
  - **46:52 - 48:26**: Visual chart schematic for Raydium/Graduated pairs:
    - Pump to $150K MCAP -> Drop 60%–70% to $20K–$50K MCAP -> Sideways consolidation -> Rebound/breakout.
  - Live Chart Examples:
    - `48:27`: Token `GME/SOL` (Pumps to 90K MCAP, dips to 20K MCAP floor, consolidates, then breaks out to 150K+ MCAP).
    - `49:07`: Token `CAR/SOL` (Pumps to 220K MCAP, drops to 38K–40K MCAP, consolidates in range, pre-breakout setup).

---

## 2. Concrete Trading Rules Table

| Rule Type | Parameter / Indicator | Exact Value / Condition | Timestamp | Bot Testable? |
| :--- | :--- | :--- | :--- | :--- |
| **Filter** | New Pairs Min Market Cap | `$3,500` | 03:29 | **Yes** |
| **Filter** | Soon (Final Stretch) Min MCAP | `$6,000` | 03:50 | **Yes** |
| **Filter** | New Pairs Holder Count | Min = `1` | 21:36 | **Yes** |
| **Entry (New Pairs)** | Dip Re-entry Level | Buy after a **50%–60% dip** from initial spike (near launch floor, e.g., $3K–$4K MCAP) after dev/bundles sell out | 26:53 | **Partly** (Requires detecting bundle exit & dip level) |
| **Take Profit (New Pairs)** | Exit Target (Conservative) | **+50% to +60% PnL** (or 2x) | 29:17 | **Yes** |
| **Stop Loss (New Pairs)** | Loss Cutoff | **-20% Mental Stop Loss** (e.g., entry at $3K MCAP, exit if price drops to $2K MCAP) | 30:56 | **Yes** |
| **Entry (Final Stretch #1)** | 40% Dip Method MCAP Threshold | Token must have reached at least **$15K MCAP** | 41:12 | **Yes** |
| **Entry (Final Stretch #1)** | 40% Dip Method Dip Depth | Buy upon a **40% to 50% pull-back** from recent local peak | 39:27 | **Yes** |
| **Take Profit (Final Stretch #1)**| Exit Target | **+50% to +100% PnL** (2x to 3x) | 40:10 | **Yes** |
| **Entry (Final Stretch #2)** | Tracked Dev Wallet Consolidation | Buy during **sideways range consolidation** at ~$10K MCAP after initial sniper dump on a proven dev token | 43:31 | **Partly** (Requires tracked dev list & range detection) |
| **Filter (Migrated Pairs)** | Token Age Range | Token age between **1 hour and 3 hours** | 47:20 | **Yes** |
| **Filter (Migrated Pairs)** | Historical Peak MCAP | Peak ATH reached between **$100K and $200K MCAP** | 47:28 | **Yes** |
| **Entry (Migrated Pairs)** | Deep Dip Consolidation | Buy during sideways consolidation after a **60%–70% dump** down to the **$20K–$50K MCAP** range | 47:35 | **Partly** (Requires range/consolidation detection) |

---

## 3. Evidence Quality & Proof Assessment

- **On-Screen Historical Charts Shown:** Yes (`GE-Sim 2.0`, `UNEMployed`, `DRE`, `DANGERSOL`, `PENNY`, `Gnome`, `GME`, `CAR`).
- **Live Trading / Execution Proof:** **None shown in this video.** The presenter uses static chart overlays on Padre Terminal to highlight past chart patterns, market cap levels, and measure percentage moves via TradingView price-range measurement tools.
- **Wallet Addresses / Full Trade History:** No wallet addresses, live execution receipts, or unedited trade logs are displayed during the presentation.
- **Sponsorship / Group Promotion:**
  - The video heavily features the **Padre Terminal** (`trade.padre.gg`).
  - No explicit paid group or paid course sales pitch is included; presenter states the series is "100% free."

---

## 4. Red Flags & Inconsistencies

1. **"Mental Stop Loss" vs. Execution Realities:** The speaker explicitly advises against setting physical stop losses (`30:58`) and instructs viewers to use a "mental stop loss at -20%." On Solana memecoins, micro-cap tokens at $3K MCAP can drop from -20% to -100% in a single block (under 400ms), making manual/mental stop-losses ineffective.
2. **Inconsistent MCAP Floor Definitions:**
   - At `03:29`, the filter for New Pairs is set to Min $3,500 MCAP.
   - At `25:34`, the presenter describes buying New Pairs at the $2,000–$3,000 MCAP level after the dip, which would be filtered out by his own $3.5K filter depending on exact timing.
3. **Subjective "Good Narrative" Prerequisite:** The technical rules (40% dip, 60% dump) rely heavily on a discretionary filter: "if the narrative is good enough." The video provides no quantitative metric for measuring "narrative quality" at runtime, making automated backtesting difficult without human intervention.
