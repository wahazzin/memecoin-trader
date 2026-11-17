# Paper bot check-in (2026-11-17 01:42 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 804 / 136 / 21 | 804 | 23% | +0.2598 | -0.2184 | **-0.1102** | -88.5971 | 14.329 (top-ups 83.24) | -89.276 | 0 | 0 |
| `m1_random` | 877 / 99 / 112 | 875 | 24% | +0.2571 | -0.2136 | **-0.0985** | -86.1663 | 15.652 (top-ups 82.11) | -86.617 | 2 | 0 |

- Exit reasons: {'take_profit': 419, 'stop_loss': 1097, 'no_volume_15m': 163}
- Sells priced by the verified curve formula because Jupiter had no route: 686
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.444, m1_random +6.131
- Circuit breakers fired: 83
- Stream gaps logged: 92071

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
