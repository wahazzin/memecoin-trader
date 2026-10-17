# Paper bot check-in (2026-10-17 00:41 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 248 / 32 / 2 | 248 | 25% | +0.2833 | -0.2141 | **-0.0898** | -22.2619 | 11.464 (top-ups 13.81) | -113.0% | 0 | 0 |
| `m1_random` | 194 / 25 / 24 | 194 | 22% | +0.2348 | -0.2113 | **-0.1147** | -22.2556 | 11.786 (top-ups 14.10) | -111.5% | 0 | 0 |

- Exit reasons: {'take_profit': 110, 'stop_loss': 289, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 146
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.982, m1_random +1.728
- Circuit breakers fired: 20
- Stream gaps logged: 15171

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
