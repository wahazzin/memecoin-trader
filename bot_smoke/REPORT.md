# Paper bot check-in (2026-10-07 21:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 18 / 2 / 1 | 10 | 30% | +0.2881 | -0.3986 | **-0.1926** | -1.9257 | 21.773 | 0.0% | 8 | 6 |
| `m1_random` | 1 / 1 / 2 | 1 | 100% | +0.3499 | +0.0000 | **+0.3499** | +0.3499 | 20.348 | 0.0% | 0 | 0 |

- Exit reasons: {'stop_loss': 6, 'take_profit': 5}
- Circuit breakers fired: 0
- Stream gaps logged: 18

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
