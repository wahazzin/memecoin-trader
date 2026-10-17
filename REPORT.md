# Paper bot check-in (2026-10-17 03:04 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 274 / 38 / 4 | 272 | 26% | +0.2853 | -0.2151 | **-0.0845** | -22.9836 | 10.884 (top-ups 13.81) | -114.4% | 2 | 0 |
| `m1_random` | 207 / 26 / 26 | 207 | 22% | +0.2409 | -0.2109 | **-0.1105** | -22.8820 | 11.158 (top-ups 14.10) | -114.6% | 0 | 0 |

- Exit reasons: {'take_profit': 127, 'stop_loss': 308, 'no_volume_15m': 44}
- Sells priced by the verified curve formula because Jupiter had no route: 162
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +1.994
- Circuit breakers fired: 20
- Stream gaps logged: 15334

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
