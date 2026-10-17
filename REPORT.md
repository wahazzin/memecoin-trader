# Paper bot check-in (2026-10-17 02:49 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 268 / 38 / 3 | 268 | 26% | +0.2870 | -0.2151 | **-0.0839** | -22.4922 | 11.536 (top-ups 13.81) | -113.0% | 0 | 0 |
| `m1_random` | 207 / 26 / 26 | 207 | 22% | +0.2409 | -0.2109 | **-0.1105** | -22.8820 | 11.158 (top-ups 14.10) | -114.6% | 0 | 0 |

- Exit reasons: {'take_profit': 125, 'stop_loss': 306, 'no_volume_15m': 44}
- Sells priced by the verified curve formula because Jupiter had no route: 161
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +1.994
- Circuit breakers fired: 20
- Stream gaps logged: 15334

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
