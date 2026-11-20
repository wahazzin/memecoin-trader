# Paper bot check-in (2026-11-20 00:48 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 872 / 155 / 21 | 870 | 22% | +0.2742 | -0.2173 | **-0.1077** | -93.7360 | 9.286 (top-ups 83.24) | -94.315 | 2 | 0 |
| `m1_random` | 940 / 106 / 114 | 939 | 25% | +0.2538 | -0.2143 | **-0.0992** | -93.1119 | 8.756 (top-ups 82.11) | -93.533 | 1 | 0 |

- Exit reasons: {'take_profit': 445, 'stop_loss': 1187, 'no_volume_15m': 176, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 757
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.650, m1_random +6.455
- Circuit breakers fired: 88
- Stream gaps logged: 97140

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
