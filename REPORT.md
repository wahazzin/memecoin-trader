# Paper bot check-in (2026-11-04 10:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 574 / 92 / 16 | 574 | 23% | +0.2672 | -0.2192 | **-0.1082** | -62.1136 | 11.910 (top-ups 54.23) | -62.689 | 0 | 0 |
| `m1_random` | 582 / 64 / 69 | 581 | 23% | +0.2564 | -0.2137 | **-0.1044** | -60.6854 | 12.907 (top-ups 53.97) | -61.221 | 1 | 0 |

- Exit reasons: {'take_profit': 286, 'stop_loss': 760, 'no_volume_15m': 109}
- Sells priced by the verified curve formula because Jupiter had no route: 436
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.402
- Circuit breakers fired: 57
- Stream gaps logged: 69462

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
