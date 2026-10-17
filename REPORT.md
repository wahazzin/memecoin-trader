# Paper bot check-in (2026-10-17 01:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 257 / 34 / 3 | 256 | 25% | +0.2923 | -0.2163 | **-0.0871** | -22.3077 | 11.414 (top-ups 13.81) | -113.0% | 1 | 0 |
| `m1_random` | 202 / 26 / 24 | 202 | 23% | +0.2409 | -0.2118 | **-0.1087** | -21.9619 | 12.078 (top-ups 14.10) | -111.5% | 0 | 0 |

- Exit reasons: {'take_profit': 118, 'stop_loss': 297, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 153
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.982, m1_random +1.941
- Circuit breakers fired: 20
- Stream gaps logged: 15257

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
