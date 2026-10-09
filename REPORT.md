# Paper bot check-in (2026-10-09 00:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 95 / 12 / 0 | 94 | 21% | +0.3398 | -0.2085 | **-0.0919** | -8.6350 | 11.347 | -44.3% | 1 | 0 |
| `m1_random` | 43 / 6 / 6 | 43 | 12% | +0.2231 | -0.2107 | **-0.1603** | -6.8931 | 13.092 | -35.0% | 0 | 0 |

- Exit reasons: {'take_profit': 31, 'stop_loss': 83, 'no_volume_15m': 23}
- Sells priced by the verified curve formula because Jupiter had no route: 63
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.340, m1_random +0.414
- Circuit breakers fired: 5
- Stream gaps logged: 793

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
