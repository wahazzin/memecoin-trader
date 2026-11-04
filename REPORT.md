# Paper bot check-in (2026-11-04 05:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 574 / 92 / 16 | 574 | 23% | +0.2672 | -0.2192 | **-0.1082** | -62.1136 | 11.910 (top-ups 54.23) | -62.689 | 0 | 0 |
| `m1_random` | 561 / 61 / 62 | 561 | 23% | +0.2625 | -0.2151 | **-0.1070** | -60.0279 | 13.787 (top-ups 53.97) | -60.468 | 0 | 0 |

- Exit reasons: {'take_profit': 278, 'stop_loss': 753, 'no_volume_15m': 104}
- Sells priced by the verified curve formula because Jupiter had no route: 426
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.144
- Circuit breakers fired: 57
- Stream gaps logged: 69393

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
