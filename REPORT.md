# Paper bot check-in (2026-10-17 02:43 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 266 / 37 / 3 | 266 | 26% | +0.2870 | -0.2151 | **-0.0830** | -22.0650 | 11.652 (top-ups 13.81) | -113.0% | 0 | 0 |
| `m1_random` | 207 / 26 / 26 | 207 | 22% | +0.2409 | -0.2109 | **-0.1105** | -22.8820 | 11.158 (top-ups 14.10) | -114.6% | 0 | 0 |

- Exit reasons: {'take_profit': 124, 'stop_loss': 305, 'no_volume_15m': 44}
- Sells priced by the verified curve formula because Jupiter had no route: 159
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +1.994
- Circuit breakers fired: 20
- Stream gaps logged: 15317

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
