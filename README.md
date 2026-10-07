# memecoin-trader (project 3)

**Paper-only** memecoin day-trader / scalper research. No real money, no wallet, no private keys:
the bot only reads public blockchain data and simulates fills.

Project 1 (equities, long-term): `quant-trading-ten-strategies-rejected`.
Project 2 (crypto AI swing trader, live paper since 2026-10-07): `crypto-ai-trader`.

## The idea in one paragraph

Most memecoins are scams or die within minutes. The traders worth learning from (see
`RESEARCH_LOG.md`, Setuh study) mostly win by **avoiding rugs**: bundled launches, dev dumps, fake
volume. So this bot is a **filter first, trader second**: code checks every new coin for scam
patterns on-chain, and only coins that pass are eligible for a simple, pre-registered entry/exit
rule. Every rule is tested alone, on data it has never seen, after realistic costs (fees, priority
fees, slippage on tiny pools), before it's trusted.

## Rules (same as the other projects)

1. Paper only. Minimum 6–8 weeks of paper trading before real money is even discussed.
2. Write the test down before looking at data (pre-registration). Design split + sealed holdout.
3. Judge by expectancy after all costs, never by win rate. Compare with doing nothing (holding SOL).
4. Every component tested alone first.
5. Never put a real wallet key or seed phrase in this repo, its secrets, or any outside code.
   Many GitHub "memecoin bots" are wallet-stealing malware; we copy none of them.

## Status

See `ROADMAP.md`. Current step: **data probe** (which free data sources work).
