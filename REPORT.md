# Paper bot check-in (2026-10-17 02:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 266 / 36 / 3 | 265 | 26% | +0.2870 | -0.2162 | **-0.0833** | -22.0621 | 11.652 (top-ups 13.81) | -113.0% | 1 | 0 |
| `m1_random` | 206 / 26 / 26 | 206 | 22% | +0.2409 | -0.2110 | **-0.1101** | -22.6787 | 11.361 (top-ups 14.10) | -113.6% | 0 | 0 |

- Exit reasons: {'take_profit': 124, 'stop_loss': 304, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 158
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +1.971
- Circuit breakers fired: 20
- Stream gaps logged: 15317

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
