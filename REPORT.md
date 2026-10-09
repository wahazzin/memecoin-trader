# Paper bot check-in (2026-10-09 00:15 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 93 / 12 / 0 | 90 | 22% | +0.3398 | -0.2057 | **-0.0845** | -7.6048 | 12.209 | -40.0% | 3 | 0 |
| `m1_random` | 41 / 6 / 6 | 40 | 12% | +0.2231 | -0.2179 | **-0.1628** | -6.5117 | 14.181 | -30.5% | 1 | 0 |

- Exit reasons: {'take_profit': 31, 'stop_loss': 78, 'no_volume_15m': 21}
- Sells priced by the verified curve formula because Jupiter had no route: 59
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.332, m1_random +0.359
- Circuit breakers fired: 4
- Stream gaps logged: 777

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
