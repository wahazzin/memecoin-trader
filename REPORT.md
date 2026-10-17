# Paper bot check-in (2026-10-17 00:21 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 243 / 31 / 2 | 243 | 25% | +0.2878 | -0.2146 | **-0.0905** | -21.9988 | 11.731 (top-ups 13.81) | -111.4% | 0 | 0 |
| `m1_random` | 193 / 24 / 24 | 193 | 22% | +0.2348 | -0.2114 | **-0.1143** | -22.0532 | 11.990 (top-ups 14.10) | -110.5% | 0 | 0 |

- Exit reasons: {'take_profit': 108, 'stop_loss': 285, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 145
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.954, m1_random +1.697
- Circuit breakers fired: 20
- Stream gaps logged: 15171

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
