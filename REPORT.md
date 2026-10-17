# Paper bot check-in (2026-10-17 02:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 265 / 36 / 3 | 264 | 27% | +0.2870 | -0.2153 | **-0.0821** | -21.6780 | 12.037 (top-ups 13.81) | -113.0% | 1 | 0 |
| `m1_random` | 205 / 26 / 25 | 205 | 22% | +0.2409 | -0.2119 | **-0.1103** | -22.6186 | 11.421 (top-ups 14.10) | -113.3% | 0 | 0 |

- Exit reasons: {'take_profit': 124, 'stop_loss': 302, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 156
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +1.971
- Circuit breakers fired: 20
- Stream gaps logged: 15317

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
