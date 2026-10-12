# Paper bot check-in (2026-10-12 02:28 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 130 / 18 / 1 | 130 | 22% | +0.3020 | -0.2158 | **-0.1003** | -13.0347 | 6.916 | -66.0% | 0 | 0 |
| `m1_random` | 99 / 13 / 14 | 98 | 19% | +0.2174 | -0.2106 | **-0.1276** | -12.5066 | 7.356 | -64.0% | 1 | 0 |

- Exit reasons: {'take_profit': 51, 'stop_loss': 146, 'no_volume_15m': 31}
- Sells priced by the verified curve formula because Jupiter had no route: 94
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.375, m1_random +0.823
- Circuit breakers fired: 11
- Stream gaps logged: 3691

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
