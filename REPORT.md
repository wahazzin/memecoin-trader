# Paper bot check-in (2026-11-22 03:58 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 922 / 165 / 21 | 922 | 23% | +0.2752 | -0.2170 | **-0.1054** | -97.1725 | 5.687 (top-ups 83.24) | -97.912 | 0 | 0 |
| `m1_random` | 962 / 108 / 114 | 962 | 25% | +0.2535 | -0.2145 | **-0.0987** | -94.9604 | 6.883 (top-ups 82.11) | -95.386 | 0 | 0 |

- Exit reasons: {'take_profit': 464, 'stop_loss': 1231, 'no_volume_15m': 188, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 797
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.729, m1_random +6.491
- Circuit breakers fired: 93
- Stream gaps logged: 101519

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
