# Paper bot check-in (2026-10-19 03:34 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 306 / 45 / 5 | 306 | 25% | +0.2906 | -0.2198 | **-0.0930** | -28.4561 | 16.938 (top-ups 25.51) | -142.1% | 0 | 0 |
| `m1_random` | 248 / 30 / 29 | 248 | 21% | +0.2634 | -0.2120 | **-0.1143** | -28.3348 | 17.299 (top-ups 25.42) | -140.3% | 0 | 0 |

- Exit reasons: {'take_profit': 135, 'stop_loss': 368, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 184
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.142, m1_random +2.098
- Circuit breakers fired: 25
- Stream gaps logged: 18381

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
