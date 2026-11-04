# Paper bot check-in (2026-11-04 00:31 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 569 / 92 / 16 | 568 | 23% | +0.2672 | -0.2193 | **-0.1080** | -61.3219 | 12.680 (top-ups 54.23) | -61.915 | 1 | 0 |
| `m1_random` | 549 / 59 / 58 | 549 | 22% | +0.2623 | -0.2160 | **-0.1088** | -59.7561 | 14.062 (top-ups 53.97) | -60.066 | 0 | 0 |

- Exit reasons: {'take_profit': 274, 'stop_loss': 743, 'no_volume_15m': 100}
- Sells priced by the verified curve formula because Jupiter had no route: 415
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.069, m1_random +4.121
- Circuit breakers fired: 56
- Stream gaps logged: 69198

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
