# Paper bot check-in (2026-11-23 06:47 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 978 / 172 / 21 | 977 | 23% | +0.2757 | -0.2146 | **-0.1017** | -99.3508 | 17.792 (top-ups 97.55) | -100.660 | 1 | 0 |
| `m1_random` | 993 / 109 / 115 | 993 | 24% | +0.2535 | -0.2134 | **-0.0991** | -98.4426 | 17.581 (top-ups 96.30) | -99.000 | 0 | 0 |

- Exit reasons: {'take_profit': 486, 'stop_loss': 1283, 'no_volume_15m': 200, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 838
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.886, m1_random +6.627
- Circuit breakers fired: 94
- Stream gaps logged: 102181

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
