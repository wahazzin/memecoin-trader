# Paper bot check-in (2026-10-12 02:03 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 130 / 18 / 1 | 130 | 22% | +0.3020 | -0.2158 | **-0.1003** | -13.0347 | 6.916 | -66.0% | 0 | 0 |
| `m1_random` | 95 / 11 / 14 | 95 | 18% | +0.2226 | -0.2116 | **-0.1339** | -12.7189 | 7.257 | -64.0% | 0 | 0 |

- Exit reasons: {'take_profit': 49, 'stop_loss': 145, 'no_volume_15m': 31}
- Sells priced by the verified curve formula because Jupiter had no route: 94
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.375, m1_random +0.820
- Circuit breakers fired: 11
- Stream gaps logged: 3645

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
