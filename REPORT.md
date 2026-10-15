# Paper bot check-in (2026-10-15 00:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 191 / 26 / 1 | 189 | 23% | +0.2857 | -0.2089 | **-0.0938** | -17.7208 | 15.986 (top-ups 13.81) | -89.3% | 2 | 0 |
| `m1_random` | 149 / 20 / 21 | 149 | 20% | +0.2342 | -0.2049 | **-0.1165** | -17.3536 | 16.704 (top-ups 14.10) | -87.1% | 0 | 0 |

- Exit reasons: {'take_profit': 77, 'stop_loss': 223, 'no_volume_15m': 38}
- Sells priced by the verified curve formula because Jupiter had no route: 120
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.670, m1_random +1.404
- Circuit breakers fired: 16
- Stream gaps logged: 7519

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
