# Paper bot check-in (2026-10-29 07:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 465 / 67 / 12 | 465 | 24% | +0.2670 | -0.2234 | **-0.1074** | -49.9275 | 9.808 (top-ups 39.90) | -50.458 | 0 | 0 |
| `m1_random` | 435 / 47 / 41 | 435 | 22% | +0.2427 | -0.2163 | **-0.1140** | -49.5803 | 9.937 (top-ups 39.64) | -49.860 | 0 | 0 |

- Exit reasons: {'take_profit': 216, 'stop_loss': 602, 'no_volume_15m': 82}
- Sells priced by the verified curve formula because Jupiter had no route: 318
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.785, m1_random +3.390
- Circuit breakers fired: 46
- Stream gaps logged: 53414

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
