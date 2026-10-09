# Paper bot check-in (2026-10-09 00:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 95 / 12 / 0 | 93 | 22% | +0.3398 | -0.2099 | **-0.0917** | -8.5282 | 11.345 | -44.3% | 2 | 0 |
| `m1_random` | 42 / 6 / 6 | 41 | 12% | +0.2231 | -0.2173 | **-0.1636** | -6.7056 | 13.300 | -34.0% | 1 | 0 |

- Exit reasons: {'take_profit': 31, 'stop_loss': 82, 'no_volume_15m': 21}
- Sells priced by the verified curve formula because Jupiter had no route: 60
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.340, m1_random +0.414
- Circuit breakers fired: 5
- Stream gaps logged: 793

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
