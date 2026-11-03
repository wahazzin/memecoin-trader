# Paper bot check-in (2026-11-03 06:49 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 559 / 86 / 15 | 559 | 23% | +0.2677 | -0.2179 | **-0.1067** | -59.6432 | 14.389 (top-ups 54.23) | -60.205 | 0 | 0 |
| `m1_random` | 545 / 57 / 58 | 543 | 23% | +0.2623 | -0.2172 | **-0.1086** | -58.9597 | 14.590 (top-ups 53.97) | -59.537 | 2 | 0 |

- Exit reasons: {'take_profit': 270, 'stop_loss': 734, 'no_volume_15m': 98}
- Sells priced by the verified curve formula because Jupiter had no route: 405
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.069, m1_random +4.050
- Circuit breakers fired: 55
- Stream gaps logged: 66442

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
