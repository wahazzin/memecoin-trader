# Paper bot check-in (2026-10-09 00:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 86 / 11 / 0 | 84 | 23% | +0.3398 | -0.2050 | **-0.0818** | -6.8705 | 13.271 | -35.0% | 2 | 0 |
| `m1_random` | 39 / 5 / 6 | 38 | 13% | +0.2231 | -0.2086 | **-0.1518** | -5.7678 | 14.292 | -30.5% | 1 | 0 |

- Exit reasons: {'take_profit': 29, 'stop_loss': 72, 'no_volume_15m': 21}
- Sells priced by the verified curve formula because Jupiter had no route: 57
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.332, m1_random +0.359
- Circuit breakers fired: 4
- Stream gaps logged: 773

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
