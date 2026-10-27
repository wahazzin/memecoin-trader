# Paper bot check-in (2026-10-27 00:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 411 / 61 / 9 | 410 | 24% | +0.2657 | -0.2240 | **-0.1070** | -43.8609 | 15.891 (top-ups 39.90) | -44.370 | 1 | 0 |
| `m1_random` | 359 / 41 / 38 | 359 | 21% | +0.2395 | -0.2178 | **-0.1197** | -42.9679 | 16.576 (top-ups 39.64) | -43.221 | 0 | 0 |

- Exit reasons: {'take_profit': 189, 'stop_loss': 517, 'no_volume_15m': 63}
- Sells priced by the verified curve formula because Jupiter had no route: 261
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.199
- Circuit breakers fired: 40
- Stream gaps logged: 47170

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
