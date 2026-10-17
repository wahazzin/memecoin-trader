# Paper bot check-in (2026-10-17 01:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 251 / 32 / 2 | 250 | 25% | +0.2928 | -0.2142 | **-0.0864** | -21.6082 | 12.095 (top-ups 13.81) | -113.0% | 1 | 0 |
| `m1_random` | 198 / 26 / 24 | 198 | 23% | +0.2400 | -0.2109 | **-0.1084** | -21.4692 | 12.571 (top-ups 14.10) | -111.5% | 0 | 0 |

- Exit reasons: {'take_profit': 114, 'stop_loss': 291, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 148
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.982, m1_random +1.909
- Circuit breakers fired: 20
- Stream gaps logged: 15210

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
