# Paper bot check-in (2026-10-15 01:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 203 / 27 / 1 | 202 | 24% | +0.2762 | -0.2090 | **-0.0937** | -18.9299 | 14.799 (top-ups 13.81) | -95.1% | 1 | 0 |
| `m1_random` | 154 / 20 / 22 | 154 | 21% | +0.2383 | -0.2045 | **-0.1096** | -16.8790 | 17.178 (top-ups 14.10) | -87.1% | 0 | 0 |

- Exit reasons: {'take_profit': 83, 'stop_loss': 233, 'no_volume_15m': 40}
- Sells priced by the verified curve formula because Jupiter had no route: 125
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.707, m1_random +1.490
- Circuit breakers fired: 16
- Stream gaps logged: 7554

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
