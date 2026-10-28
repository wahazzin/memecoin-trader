# Paper bot check-in (2026-10-28 00:56 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 441 / 64 / 11 | 440 | 24% | +0.2704 | -0.2250 | **-0.1079** | -47.4698 | 12.692 (top-ups 39.90) | -47.705 | 1 | 0 |
| `m1_random` | 396 / 44 / 38 | 395 | 22% | +0.2506 | -0.2170 | **-0.1151** | -45.4833 | 14.449 (top-ups 39.64) | -46.199 | 1 | 0 |

- Exit reasons: {'take_profit': 203, 'stop_loss': 560, 'no_volume_15m': 72}
- Sells priced by the verified curve formula because Jupiter had no route: 287
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.682, m1_random +3.319
- Circuit breakers fired: 42
- Stream gaps logged: 50136

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
