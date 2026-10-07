# Measured costs of real pump.fun trades (2026-10-07 20:28 UTC)

Listened 4 min: 9919 single-trade transactions (1745 with 0 fee in the event). Fetched 430, usable 178, skipped {'no_tx': 160, 'payer_is_not_trader': 92}.

All amounts in SOL. Percent columns = cost as % of the trade size. Medians (p50) and p90.

| Group | n | pump+creator fee % | priority fee SOL p50 / p90 | Jito tip SOL p50 / p90 | new-account rent SOL (share of trades paying it) | unexplained SOL p50 / p90 | **total overhead % of size p50 / p90** |
|---|---|---|---|---|---|---|---|
| buys < 0.2 SOL | 40 | 1.25% | 0.000025 / 0.000500 | 0.000000 / 0.000000 | 0.001514 (70%) | 0.000005 / 0.009606 | **2.23% / 332.74%** |
| buys 0.2–1 SOL | 29 | 1.25% | 0.000050 / 0.001500 | 0.000000 / 0.000000 | 0.002039 (59%) | 0.000843 / 0.006926 | **0.43% / 3.98%** |
| buys ≥ 1 SOL | 11 | 1.25% | 0.000050 / 0.003200 | 0.000000 / 0.000000 | 0.002860 (91%) | 0.001100 / 0.017500 | **0.38% / 1.27%** |
| sells (all sizes) | 98 | 1.25% | 0.000060 / 0.000700 | 0.000000 / 0.000000 | 0.001488 (9%) | 0.000000 / 0.002000 | **0.28% / 3.31%** |
| event shows 0 fee | 0 | | | | | | |

Overhead = network + priority + Jito tip + new-account rent + unexplained (if positive). Pump/creator fees are separate (in the Jupiter quote). Rent is refundable only if the account is closed later.
