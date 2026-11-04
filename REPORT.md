# Paper bot check-in (2026-11-04 00:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 574 / 92 / 16 | 573 | 23% | +0.2672 | -0.2197 | **-0.1084** | -62.0941 | 11.908 (top-ups 54.23) | -62.689 | 1 | 0 |
| `m1_random` | 550 / 60 / 59 | 550 | 22% | +0.2623 | -0.2161 | **-0.1091** | -60.0159 | 13.800 (top-ups 53.97) | -60.327 | 0 | 0 |

- Exit reasons: {'take_profit': 276, 'stop_loss': 746, 'no_volume_15m': 101}
- Sells priced by the verified curve formula because Jupiter had no route: 419
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.121
- Circuit breakers fired: 57
- Stream gaps logged: 69208

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
