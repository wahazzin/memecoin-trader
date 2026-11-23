# Paper bot check-in (2026-11-23 03:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 952 / 167 / 21 | 951 | 23% | +0.2783 | -0.2154 | **-0.1033** | -98.2123 | 18.923 (top-ups 97.55) | -100.426 | 1 | 0 |
| `m1_random` | 985 / 109 / 114 | 985 | 24% | +0.2545 | -0.2137 | **-0.0996** | -98.1047 | 18.176 (top-ups 96.30) | -98.276 | 0 | 0 |

- Exit reasons: {'take_profit': 473, 'stop_loss': 1268, 'no_volume_15m': 194, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 822
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.772, m1_random +6.625
- Circuit breakers fired: 94
- Stream gaps logged: 102121

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
