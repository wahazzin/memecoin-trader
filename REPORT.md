# Paper bot check-in (2026-10-24 00:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 376 / 55 / 7 | 375 | 25% | +0.2647 | -0.2213 | **-0.1007** | -37.7783 | 7.590 (top-ups 25.51) | -188.0% | 1 | 0 |
| `m1_random` | 325 / 37 / 36 | 324 | 22% | +0.2482 | -0.2138 | **-0.1140** | -36.9223 | 8.096 (top-ups 25.42) | -185.9% | 1 | 0 |

- Exit reasons: {'take_profit': 175, 'stop_loss': 466, 'no_volume_15m': 58}
- Sells priced by the verified curve formula because Jupiter had no route: 230
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.343, m1_random +2.978
- Circuit breakers fired: 34
- Stream gaps logged: 33244

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
