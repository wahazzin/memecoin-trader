# Paper bot check-in (2026-10-23 02:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 368 / 53 / 7 | 368 | 25% | +0.2620 | -0.2201 | **-0.1009** | -37.1347 | 8.240 (top-ups 25.51) | -184.8% | 0 | 0 |
| `m1_random` | 322 / 37 / 35 | 322 | 22% | +0.2482 | -0.2128 | **-0.1126** | -36.2583 | 9.071 (top-ups 25.42) | -181.1% | 0 | 0 |

- Exit reasons: {'take_profit': 172, 'stop_loss': 460, 'no_volume_15m': 58}
- Sells priced by the verified curve formula because Jupiter had no route: 226
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.342, m1_random +2.974
- Circuit breakers fired: 33
- Stream gaps logged: 30723

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
