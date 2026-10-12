# Paper bot check-in (2026-10-12 18:04 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 130 / 18 / 1 | 130 | 22% | +0.3020 | -0.2158 | **-0.1003** | -13.0347 | 6.916 | -66.0% | 0 | 0 |
| `m1_random` | 103 / 13 / 14 | 103 | 19% | +0.2167 | -0.2080 | **-0.1255** | -12.9303 | 7.043 | -65.1% | 0 | 0 |

- Exit reasons: {'take_profit': 52, 'stop_loss': 149, 'no_volume_15m': 32}
- Sells priced by the verified curve formula because Jupiter had no route: 95
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.375, m1_random +0.825
- Circuit breakers fired: 12
- Stream gaps logged: 4643

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
