# Paper bot check-in (2026-10-17 01:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 255 / 33 / 3 | 255 | 25% | +0.2923 | -0.2166 | **-0.0869** | -22.1611 | 11.562 (top-ups 13.81) | -113.0% | 0 | 0 |
| `m1_random` | 200 / 26 / 24 | 200 | 23% | +0.2409 | -0.2124 | **-0.1081** | -21.6234 | 12.417 (top-ups 14.10) | -111.5% | 0 | 0 |

- Exit reasons: {'take_profit': 117, 'stop_loss': 295, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 152
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.982, m1_random +1.936
- Circuit breakers fired: 20
- Stream gaps logged: 15229

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
