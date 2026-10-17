# Paper bot check-in (2026-10-17 12:14 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 275 / 38 / 4 | 275 | 26% | +0.2818 | -0.2164 | **-0.0859** | -23.6298 | 10.083 (top-ups 13.81) | -118.3% | 0 | 0 |
| `m1_random` | 211 / 26 / 26 | 211 | 22% | +0.2409 | -0.2114 | **-0.1128** | -23.7948 | 10.245 (top-ups 14.10) | -119.1% | 0 | 0 |

- Exit reasons: {'take_profit': 127, 'stop_loss': 312, 'no_volume_15m': 47}
- Sells priced by the verified curve formula because Jupiter had no route: 165
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +2.038
- Circuit breakers fired: 22
- Stream gaps logged: 15480

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
