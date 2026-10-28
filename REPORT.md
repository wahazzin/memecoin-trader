# Paper bot check-in (2026-10-28 21:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 442 / 64 / 11 | 442 | 24% | +0.2704 | -0.2249 | **-0.1084** | -47.9068 | 11.833 (top-ups 39.90) | -48.428 | 0 | 0 |
| `m1_random` | 410 / 44 / 39 | 410 | 22% | +0.2454 | -0.2181 | **-0.1164** | -47.7082 | 11.813 (top-ups 39.64) | -47.983 | 0 | 0 |

- Exit reasons: {'take_profit': 205, 'stop_loss': 573, 'no_volume_15m': 74}
- Sells priced by the verified curve formula because Jupiter had no route: 291
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.700, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52420

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
