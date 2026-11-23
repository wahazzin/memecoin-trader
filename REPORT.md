# Paper bot check-in (2026-11-23 19:54 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 982 / 172 / 21 | 982 | 23% | +0.2750 | -0.2148 | **-0.1021** | -100.2717 | 16.878 (top-ups 97.55) | -101.034 | 0 | 0 |
| `m1_random` | 998 / 110 / 115 | 998 | 24% | +0.2533 | -0.2134 | **-0.0993** | -99.0938 | 16.928 (top-ups 96.30) | -99.524 | 0 | 0 |

- Exit reasons: {'take_profit': 488, 'stop_loss': 1290, 'no_volume_15m': 201, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 840
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.886, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 103343

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
