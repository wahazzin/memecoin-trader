# Paper bot check-in (2026-11-04 00:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 563 / 89 / 16 | 563 | 23% | +0.2686 | -0.2189 | **-0.1072** | -60.3691 | 14.424 (top-ups 54.23) | -60.205 | 0 | 0 |
| `m1_random` | 547 / 58 / 58 | 547 | 22% | +0.2623 | -0.2164 | **-0.1088** | -59.4991 | 14.322 (top-ups 53.97) | -59.810 | 0 | 0 |

- Exit reasons: {'take_profit': 272, 'stop_loss': 738, 'no_volume_15m': 100}
- Sells priced by the verified curve formula because Jupiter had no route: 411
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.069, m1_random +4.121
- Circuit breakers fired: 56
- Stream gaps logged: 69166

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
