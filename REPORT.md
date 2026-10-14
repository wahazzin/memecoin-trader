# Paper bot check-in (2026-10-14 02:05 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 163 / 22 / 1 | 163 | 24% | +0.2903 | -0.2120 | **-0.0918** | -14.9646 | 18.790 (top-ups 13.81) | -77.5% | 0 | 0 |
| `m1_random` | 121 / 15 / 18 | 121 | 20% | +0.2387 | -0.2058 | **-0.1177** | -14.2374 | 19.830 (top-ups 14.10) | -71.6% | 0 | 0 |

- Exit reasons: {'take_profit': 65, 'stop_loss': 182, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 110
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.556, m1_random +0.996
- Circuit breakers fired: 14
- Stream gaps logged: 6313

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
