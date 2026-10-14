# Paper bot check-in (2026-10-14 02:36 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 169 / 22 / 1 | 169 | 24% | +0.2893 | -0.2094 | **-0.0914** | -15.4408 | 18.314 (top-ups 13.81) | -77.9% | 0 | 0 |
| `m1_random` | 124 / 15 / 18 | 124 | 19% | +0.2387 | -0.2065 | **-0.1204** | -14.9254 | 19.142 (top-ups 14.10) | -75.0% | 0 | 0 |

- Exit reasons: {'take_profit': 66, 'stop_loss': 190, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 110
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.579, m1_random +1.009
- Circuit breakers fired: 14
- Stream gaps logged: 6313

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
