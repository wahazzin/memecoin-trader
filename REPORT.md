# Paper bot check-in (2026-11-21 00:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 879 / 156 / 21 | 879 | 22% | +0.2721 | -0.2169 | **-0.1078** | -94.7840 | 8.067 (top-ups 83.24) | -95.532 | 0 | 0 |
| `m1_random` | 942 / 106 / 114 | 942 | 25% | +0.2528 | -0.2143 | **-0.0993** | -93.5164 | 8.332 (top-ups 82.11) | -93.938 | 0 | 0 |

- Exit reasons: {'take_profit': 445, 'stop_loss': 1193, 'no_volume_15m': 182, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 766
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.650, m1_random +6.455
- Circuit breakers fired: 90
- Stream gaps logged: 100238

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
