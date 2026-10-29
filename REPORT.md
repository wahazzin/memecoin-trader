# Paper bot check-in (2026-10-29 00:20 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 447 / 64 / 11 | 447 | 23% | +0.2704 | -0.2238 | **-0.1077** | -48.1462 | 11.594 (top-ups 39.90) | -48.877 | 0 | 0 |
| `m1_random` | 412 / 44 / 39 | 412 | 22% | +0.2463 | -0.2176 | **-0.1152** | -47.4459 | 12.076 (top-ups 39.64) | -47.983 | 0 | 0 |

- Exit reasons: {'take_profit': 207, 'stop_loss': 578, 'no_volume_15m': 74}
- Sells priced by the verified curve formula because Jupiter had no route: 294
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.713, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52807

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
