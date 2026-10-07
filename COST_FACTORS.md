# COST & RISK FACTORS — every one a real trade has, and how paper trading gets it

Owner rule (2026-10-07): **nothing assumed.** Every factor is either taken from a live real source
(Jupiter quote / the blockchain), measured from our own recorded data, or listed as NOT covered.
A factor without a ✅ blocks going live. If we find a new factor, it gets added here with the date.

| # | Factor | What it is (ELI5) | How paper trading gets it | Status |
|---|---|---|---|---|
| 1 | Pump.fun protocol fee | pump.fun takes 0.95% of every buy and sell | Inside the live Jupiter quote. Cross-check: read from on-chain trade events (measured 0.95%) | ✅ in quote, verified on-chain |
| 2 | Creator fee | the coin's creator gets 0.30% of every trade | Same as #1 (measured 0.30% on-chain) | ✅ in quote, verified on-chain |
| 3 | Price impact | your own buy pushes the price up before it's done | Inside the Jupiter quote for that exact size | ✅ in quote |
| 4 | Pool / route fees after migration | coins that graduate trade on PumpSwap, which has its own fee | Inside the Jupiter quote (route "Pump.fun Amm") | ✅ in quote |
| 5 | Can't sell at all | sometimes there is no buyer route | Jupiter returns "no route" → paper position stays stuck, counted as stuck (seen in probe 3: 2 of 8 coins) | ✅ live |
| 6 | Solana network fee | 0.000005 SOL per transaction | Exact protocol constant, added to every trade | ✅ exact |
| 7 | **Priority fee** | extra tip so your trade gets in fast; memecoin traders pay it on every trade | **Measured** from real transactions in our data (what other traders actually paid in the same minute), charged at that rate | ⬜ to build: needs transaction lookups |
| 8 | **Token account rent** | the first time you buy a coin, Solana charges ~0.002 SOL to open a "slot" for it. Refunded only if you close it later. On a 0.1 SOL trade that's **2%** | Exact protocol amount, charged on every new coin; refund only counted if the bot closes the account | ⬜ to build (exact number, read from chain) |
| 9 | **Delay (latency)** | the price moves in the 1–3 seconds between deciding and the trade landing | Ask Jupiter again after the measured landing delay, and fill at **that** quote, not the first one | ⬜ to build (real second quote) |
| 10 | **Failed transactions** | if the price jumps past your slippage limit, the trade fails but you still pay fees | Counted when the second quote (#9) is worse than the slippage limit: trade marked failed, fees charged | ⬜ to build |
| 11 | **Sandwich bots (MEV)** | a bot buys right before you and sells right after, so you pay more | Partly measurable: how often recorded trades of our size get sandwiched (same wallet buys before / sells after in the same block) → charged at the measured rate | ⬜ to measure; may stay "partly covered" |
| 12 | Terminal / bot fee | Axiom, Photon etc. add ~0.75–1% per trade | Only applies if we ever trade through a terminal. Direct Jupiter API = 0. Must match the real execution path at go-live | ✅ 0 for API path; flagged for go-live |
| 13 | Token taxes | some coins (not standard pump.fun) take a % on every transfer | Read the coin's token program on-chain; coins with transfer fees are skipped or charged exactly | ⬜ to build |
| 14 | Rugs, dev dumps, liquidity pulls | the coin goes to zero | Live price via Jupiter: a rug shows up as a terrible or impossible sell | ✅ live |
| 15 | Bot downtime | our paper bot misses moments it was offline | Every gap logged; trades open during a gap valued at the first price after it | ✅ logged |
| 16 | SOL price moves | profits in SOL can be losses in dollars | Report P&L in SOL **and** USD | ⬜ in the report |
| 17 | Being first vs other bots | would a real order land before the competition? | **NOT coverable by any paper trading.** Only tiny real trades can show it, and only after the paper phase | ❌ stated, not modelled |
| 18 | Tax (Sweden) | profit on crypto is taxed (capital gains) at go-live | Not a trading cost; must be in the go-live decision | 📌 go-live checklist |

## How we check the paper fills are honest (before anything goes live)

1. **Fee audit:** every paper trade's fees are compared with the fees on real trades of the same coin in
   the same minute, from our recorder. They must match.
2. **Fill audit:** at random moments, compare the Jupiter quote with real trades of similar size that
   actually landed in the next few seconds (recorded on-chain). The gap is reported every week. If paper
   fills are systematically better than real fills, every result is corrected by that gap.
3. **New factor rule:** anything we discover later gets a row here and is applied to ALL past paper
   trades retroactively before any verdict.
