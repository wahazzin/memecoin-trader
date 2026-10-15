# Paper bot check-in (2026-10-15 20:29 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 206 / 27 / 1 | 206 | 23% | +0.2762 | -0.2077 | **-0.0949** | -19.5548 | 14.188 (top-ups 13.81) | -98.2% | 0 | 0 |
| `m1_random` | 168 / 22 / 23 | 168 | 20% | +0.2370 | -0.2077 | **-0.1177** | -19.7738 | 14.277 (top-ups 14.10) | -99.1% | 0 | 0 |

- Exit reasons: {'take_profit': 84, 'stop_loss': 249, 'no_volume_15m': 41}
- Sells priced by the verified curve formula because Jupiter had no route: 128
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.716, m1_random +1.549
- Circuit breakers fired: 18
- Stream gaps logged: 8540

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
