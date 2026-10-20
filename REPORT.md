# Paper bot check-in (2026-10-20 01:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 324 / 47 / 6 | 324 | 26% | +0.2756 | -0.2212 | **-0.0940** | -30.4456 | 14.943 (top-ups 25.51) | -152.2% | 0 | 0 |
| `m1_random` | 253 / 31 / 29 | 253 | 21% | +0.2627 | -0.2126 | **-0.1149** | -29.0696 | 16.278 (top-ups 25.42) | -146.5% | 0 | 0 |

- Exit reasons: {'take_profit': 141, 'stop_loss': 385, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 197
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.210, m1_random +2.234
- Circuit breakers fired: 26
- Stream gaps logged: 20678

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
