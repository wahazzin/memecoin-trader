# Paper bot check-in (2026-10-14 07:14 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 176 / 22 / 1 | 176 | 23% | +0.2893 | -0.2097 | **-0.0963** | -16.9428 | 16.812 (top-ups 13.81) | -85.3% | 0 | 0 |
| `m1_random` | 144 / 19 / 21 | 144 | 20% | +0.2338 | -0.2061 | **-0.1175** | -16.9213 | 17.140 (top-ups 14.10) | -84.9% | 0 | 0 |

- Exit reasons: {'take_profit': 71, 'stop_loss': 212, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 115
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.632, m1_random +1.398
- Circuit breakers fired: 15
- Stream gaps logged: 6416

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
