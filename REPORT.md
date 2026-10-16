# Paper bot check-in (2026-10-16 01:54 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 240 / 31 / 2 | 239 | 25% | +0.2887 | -0.2129 | **-0.0891** | -21.2995 | 12.548 (top-ups 13.81) | -106.2% | 1 | 0 |
| `m1_random` | 180 / 24 / 24 | 180 | 21% | +0.2383 | -0.2095 | **-0.1150** | -20.6919 | 13.353 (top-ups 14.10) | -103.7% | 0 | 0 |

- Exit reasons: {'take_profit': 103, 'stop_loss': 274, 'no_volume_15m': 42}
- Sells priced by the verified curve formula because Jupiter had no route: 142
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.947, m1_random +1.589
- Circuit breakers fired: 18
- Stream gaps logged: 9307

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
