# Paper bot check-in (2026-10-20 00:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 311 / 47 / 5 | 311 | 25% | +0.2850 | -0.2205 | **-0.0937** | -29.1513 | 16.239 (top-ups 25.51) | -145.5% | 0 | 0 |
| `m1_random` | 249 / 30 / 29 | 249 | 20% | +0.2634 | -0.2118 | **-0.1144** | -28.4976 | 16.853 (top-ups 25.42) | -142.5% | 0 | 0 |

- Exit reasons: {'take_profit': 136, 'stop_loss': 373, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 186
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.206, m1_random +2.145
- Circuit breakers fired: 26
- Stream gaps logged: 20653

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
