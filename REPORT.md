# Paper bot check-in (2026-11-03 05:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 559 / 86 / 15 | 559 | 23% | +0.2677 | -0.2179 | **-0.1067** | -59.6432 | 14.389 (top-ups 54.23) | -60.205 | 0 | 0 |
| `m1_random` | 537 / 57 / 58 | 537 | 23% | +0.2582 | -0.2181 | **-0.1099** | -59.0282 | 14.792 (top-ups 53.97) | -59.335 | 0 | 0 |

- Exit reasons: {'take_profit': 269, 'stop_loss': 730, 'no_volume_15m': 97}
- Sells priced by the verified curve formula because Jupiter had no route: 402
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.069, m1_random +4.012
- Circuit breakers fired: 55
- Stream gaps logged: 66380

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
