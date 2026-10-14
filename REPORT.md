# Paper bot check-in (2026-10-14 03:21 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 176 / 22 / 1 | 176 | 23% | +0.2893 | -0.2097 | **-0.0963** | -16.9428 | 17.079 (top-ups 13.81) | -83.9% | 0 | 0 |
| `m1_random` | 127 / 16 / 19 | 127 | 19% | +0.2387 | -0.2069 | **-0.1227** | -15.5866 | 18.481 (top-ups 14.10) | -78.3% | 0 | 0 |

- Exit reasons: {'take_profit': 66, 'stop_loss': 200, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 114
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.632, m1_random +1.064
- Circuit breakers fired: 15
- Stream gaps logged: 6403

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
