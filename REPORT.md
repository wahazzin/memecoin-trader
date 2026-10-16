# Paper bot check-in (2026-10-16 03:06 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 241 / 31 / 2 | 241 | 24% | +0.2887 | -0.2136 | **-0.0906** | -21.8369 | 11.892 (top-ups 13.81) | -109.4% | 0 | 0 |
| `m1_random` | 188 / 24 / 24 | 188 | 22% | +0.2360 | -0.2087 | **-0.1117** | -21.0022 | 13.081 (top-ups 14.10) | -106.9% | 0 | 0 |

- Exit reasons: {'take_profit': 106, 'stop_loss': 281, 'no_volume_15m': 42}
- Sells priced by the verified curve formula because Jupiter had no route: 144
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.948, m1_random +1.669
- Circuit breakers fired: 19
- Stream gaps logged: 9430

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
