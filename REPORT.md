# Paper bot check-in (2026-10-14 02:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 164 / 22 / 1 | 164 | 24% | +0.2893 | -0.2120 | **-0.0897** | -14.7141 | 19.041 (top-ups 13.81) | -77.5% | 0 | 0 |
| `m1_random` | 124 / 15 / 18 | 123 | 20% | +0.2387 | -0.2072 | **-0.1202** | -14.7879 | 19.196 (top-ups 14.10) | -74.7% | 1 | 0 |

- Exit reasons: {'take_profit': 66, 'stop_loss': 184, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 110
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.556, m1_random +0.996
- Circuit breakers fired: 14
- Stream gaps logged: 6313

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
