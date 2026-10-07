# Paper bot check-in (2026-10-07 21:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 23 / 4 / 1 | 14 | 21% | +0.2881 | -0.3573 | **-0.2190** | -3.0664 | 16.865 | -22.5% | 9 | 8 |
| `m1_random` | 8 / 1 / 3 | 6 | 33% | +0.3667 | -0.2454 | **-0.0413** | -0.2480 | 19.718 | -3.2% | 2 | 0 |

- Exit reasons: {'stop_loss': 14, 'take_profit': 6}
- Sells priced by the verified curve formula because Jupiter had no route: 3
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.009, m1_random +0.000
- Circuit breakers fired: 1
- Stream gaps logged: 24

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
