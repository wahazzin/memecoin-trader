# Paper bot check-in (2026-10-28 00:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 436 / 64 / 10 | 436 | 24% | +0.2631 | -0.2244 | **-0.1092** | -47.6231 | 12.557 (top-ups 39.90) | -47.705 | 0 | 0 |
| `m1_random` | 393 / 44 / 38 | 392 | 22% | +0.2440 | -0.2169 | **-0.1170** | -45.8479 | 13.598 (top-ups 39.64) | -46.199 | 1 | 0 |

- Exit reasons: {'take_profit': 201, 'stop_loss': 555, 'no_volume_15m': 72}
- Sells priced by the verified curve formula because Jupiter had no route: 283
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.682, m1_random +3.319
- Circuit breakers fired: 42
- Stream gaps logged: 50136

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
