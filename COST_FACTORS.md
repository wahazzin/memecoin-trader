# COST & RISK FACTORS — every one a real trade has, and how paper trading gets it

Owner rule (2026-10-07): **nothing assumed.** Every factor is either taken from a live real source
(Jupiter quote / the blockchain), measured from our own recorded data, or listed as NOT covered.
A factor without a ✅ blocks going live. If we find a new factor, it gets added here with the date.

| # | Factor | What it is (ELI5) | How paper trading gets it | Status |
|---|---|---|---|---|
| 1 | Pump.fun protocol fee | pump.fun takes 0.95% of every buy and sell | Inside the live Jupiter quote. Cross-check: read from on-chain trade events (measured 0.95%) | ✅ in quote, verified on-chain |
| 2 | Creator fee | the coin's creator gets a cut of every trade: **0.30% on most coins, but 1%, 1.8%, 2% or 3% on some** (measured: 986 / 1,004 coins at 0.30%) | Same as #1, per coin. A 3% creator fee = 6.6% round trip, so the bot reads each coin's rate and the filter can skip high-fee coins | ✅ in quote, verified on-chain |
| 3 | Price impact | your own buy pushes the price up before it's done | Inside the Jupiter quote for that exact size | ✅ in quote |
| 4 | Pool / route fees after migration | coins that graduate trade on PumpSwap, which has its own fee | Inside the Jupiter quote (route "Pump.fun Amm") | ✅ in quote |
| 5 | Can't sell at all | on pump.fun's curve you can ALWAYS sell before the coin graduates (the curve is the buyer); after graduation it depends on the pool | Smoke tests 2026-10-07/08: **Jupiter had no sell route for ~70% of fresh coins that were still trading on their curve** (a Jupiter coverage gap, not the market). Then the sell is priced from the coin's live on-chain curve account with the curve formula (= Jupiter to 0.0000%), marked `curve_formula` in every order. Graduated coins with no route stay stuck and are reported | ✅ live, marked |
| 6 | Solana network fee | 0.000005 SOL per transaction | Exact protocol constant, added to every trade | ✅ exact |
| 7 | **Priority fee** | extra tip so your trade gets in fast; memecoin traders pay it on every trade | **Measured 2026-10-07** from 178 real trades (`research/measure_costs.py`): median 0.00005 SOL, p90 0.0015–0.003 SOL per trade. Paper bot charges the p90 (pessimistic) until re-measured; re-measured weekly | ✅ measured |
| 8 | **Token account rent** | the first time you buy a coin, Solana charges ~0.002 SOL to open a "slot" for it. Refunded only if you close it later. On a 0.1 SOL trade that's **2%** | **Measured**: 0.0015–0.0029 SOL, paid on 60–90% of real buys. Paper bot charges 0.00204 SOL (the token-account rent) on every first buy of a coin and refunds it only when it closes the account after selling | ✅ measured |
| 9 | **Delay (latency)** | the price moves in the 1–3 seconds between deciding and the trade landing | Ask Jupiter again after the measured landing delay, and fill at **that** quote, not the first one | ⬜ to build (real second quote) |
| 10 | **Failed transactions** | if the price jumps past your slippage limit, the trade fails but you still pay fees | Counted when the second quote (#9) is worse than the slippage limit: trade marked failed, fees charged | ⬜ to build |
| 11 | **Sandwich bots (MEV)** | a bot buys right before you and sells right after, so you pay more | Partly measurable: how often recorded trades of our size get sandwiched (same wallet buys before / sells after in the same block) → charged at the measured rate | ⬜ to measure; may stay "partly covered" |
| 12 | Terminal / bot fee + non-Jito tips | Axiom, Photon etc. add ~0.75–1% per trade; some traders tip other speed services | **Measured as "unexplained" SOL** on real trades: median ~0.001 SOL, p90 ~1% of trade size on buys (consistent with terminal fees). Direct Jupiter API path = 0 terminal fee; tips to speed services stay a go-live question | ✅ measured; go-live path must match |
| 13 | Token taxes | some coins (not standard pump.fun) take a % on every transfer | Read the coin's token program on-chain; coins with transfer fees are skipped or charged exactly | ⬜ to build |
| 14 | Rugs, dev dumps, liquidity pulls | the coin goes to zero | Live price via Jupiter: a rug shows up as a terrible or impossible sell | ✅ live |
| 15 | Bot downtime | our paper bot misses moments it was offline | Every gap logged; trades open during a gap valued at the first price after it | ✅ logged |
| 16 | SOL price moves | profits in SOL can be losses in dollars | Report P&L in SOL **and** USD | ⬜ in the report |
| 17 | Being first vs other bots | would a real order land before the competition? | **NOT coverable by any paper trading.** Only tiny real trades can show it, and only after the paper phase | ❌ stated, not modelled |
| 18 | Tax (Sweden) | profit on crypto is taxed (capital gains) at go-live | Not a trading cost; must be in the go-live decision | 📌 go-live checklist |

## Measured all-in overhead (2026-10-07, 178 real trades)

On top of the 1.25% pump.fun + creator fee per side:

| Trade size | Extra overhead per buy, median / p90 |
|---|---|
| < 0.2 SOL | **2.2%** / very high (rent + priority on a tiny trade) |
| 0.2–1 SOL | 0.4% / 4.0% |
| ≥ 1 SOL | 0.4% / 1.3% |
| sells | 0.3% / 3.3% |

**Lesson:** a 0.1 SOL scalp costs roughly **4.5–5% round trip** all-in. A 0.5 SOL one costs about 3%.
Tiny trades are eaten by fixed costs, which is why Setuh says under 0.1 SOL "gets demolished by fees".

## How we check the paper fills are honest (before anything goes live)

1. **Fee audit:** every paper trade's fees are compared with the fees on real trades of the same coin in
   the same minute, from our recorder. They must match.
2. **Fill audit:** at random moments, compare the Jupiter quote with real trades of similar size that
   actually landed in the next few seconds (recorded on-chain). The gap is reported every week. If paper
   fills are systematically better than real fills, every result is corrected by that gap.
3. **New factor rule:** anything we discover later gets a row here and is applied to ALL past paper
   trades retroactively before any verdict.
