# Paper bot check-in (2026-10-26 00:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 396 / 57 / 9 | 396 | 24% | +0.2624 | -0.2215 | **-0.1029** | -40.7655 | 19.005 (top-ups 39.90) | -202.6% | 0 | 0 |
| `m1_random` | 337 / 39 / 38 | 337 | 21% | +0.2450 | -0.2175 | **-0.1187** | -39.9869 | 19.560 (top-ups 39.64) | -199.6% | 0 | 0 |

- Exit reasons: {'take_profit': 181, 'stop_loss': 491, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 243
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.137
- Circuit breakers fired: 38
- Stream gaps logged: 42442

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
