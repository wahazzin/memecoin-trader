# Paper bot check-in (2026-11-06 03:16 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 598 / 95 / 16 | 598 | 22% | +0.2673 | -0.2190 | **-0.1100** | -65.7860 | 8.227 (top-ups 54.23) | -66.368 | 0 | 0 |
| `m1_random` | 661 / 74 / 82 | 661 | 24% | +0.2550 | -0.2114 | **-0.0978** | -64.6531 | 9.134 (top-ups 53.97) | -64.993 | 0 | 0 |

- Exit reasons: {'take_profit': 312, 'stop_loss': 825, 'no_volume_15m': 122}
- Sells priced by the verified curve formula because Jupiter had no route: 477
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.759
- Circuit breakers fired: 61
- Stream gaps logged: 74267

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
