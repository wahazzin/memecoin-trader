# Paper bot check-in (2026-10-27 00:47 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 419 / 61 / 9 | 419 | 24% | +0.2657 | -0.2242 | **-0.1084** | -45.4280 | 14.321 (top-ups 39.90) | -45.940 | 0 | 0 |
| `m1_random` | 361 / 41 / 38 | 361 | 22% | +0.2392 | -0.2171 | **-0.1185** | -42.7758 | 16.768 (top-ups 39.64) | -43.247 | 0 | 0 |

- Exit reasons: {'take_profit': 191, 'stop_loss': 524, 'no_volume_15m': 65}
- Sells priced by the verified curve formula because Jupiter had no route: 266
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.199
- Circuit breakers fired: 40
- Stream gaps logged: 47282

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
