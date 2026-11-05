# Paper bot check-in (2026-11-05 10:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 584 / 92 / 16 | 584 | 22% | +0.2672 | -0.2187 | **-0.1097** | -64.0666 | 9.957 (top-ups 54.23) | -64.638 | 0 | 0 |
| `m1_random` | 622 / 69 / 76 | 621 | 24% | +0.2566 | -0.2110 | **-0.0988** | -61.3842 | 12.505 (top-ups 53.97) | -62.959 | 1 | 0 |

- Exit reasons: {'take_profit': 299, 'stop_loss': 791, 'no_volume_15m': 115}
- Sells priced by the verified curve formula because Jupiter had no route: 458
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.524
- Circuit breakers fired: 59
- Stream gaps logged: 71698

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
