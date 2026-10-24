# Paper bot check-in (2026-10-24 00:21 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 373 / 54 / 7 | 373 | 25% | +0.2647 | -0.2212 | **-0.1001** | -37.3307 | 8.040 (top-ups 25.51) | -187.2% | 0 | 0 |
| `m1_random` | 324 / 37 / 36 | 324 | 22% | +0.2482 | -0.2138 | **-0.1140** | -36.9223 | 8.407 (top-ups 25.42) | -184.4% | 0 | 0 |

- Exit reasons: {'take_profit': 174, 'stop_loss': 465, 'no_volume_15m': 58}
- Sells priced by the verified curve formula because Jupiter had no route: 229
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.343, m1_random +2.978
- Circuit breakers fired: 34
- Stream gaps logged: 33230

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
