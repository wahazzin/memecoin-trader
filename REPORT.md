# Paper bot check-in (2026-10-16 00:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 216 / 29 / 1 | 215 | 24% | +0.2887 | -0.2085 | **-0.0883** | -18.9770 | 14.178 (top-ups 13.81) | -101.4% | 1 | 0 |
| `m1_random` | 170 / 23 / 23 | 169 | 20% | +0.2370 | -0.2089 | **-0.1192** | -20.1439 | 13.811 (top-ups 14.10) | -101.4% | 1 | 0 |

- Exit reasons: {'take_profit': 89, 'stop_loss': 254, 'no_volume_15m': 41}
- Sells priced by the verified curve formula because Jupiter had no route: 135
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.753, m1_random +1.549
- Circuit breakers fired: 18
- Stream gaps logged: 8929

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
