# Paper bot check-in (2026-10-16 00:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 218 / 29 / 1 | 216 | 24% | +0.2887 | -0.2087 | **-0.0889** | -19.2050 | 14.854 (top-ups 13.81) | -101.4% | 2 | 0 |
| `m1_random` | 173 / 23 / 23 | 170 | 21% | +0.2352 | -0.2089 | **-0.1175** | -19.9694 | 13.793 (top-ups 14.10) | -101.5% | 3 | 0 |

- Exit reasons: {'take_profit': 90, 'stop_loss': 255, 'no_volume_15m': 41}
- Sells priced by the verified curve formula because Jupiter had no route: 135
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.812, m1_random +1.549
- Circuit breakers fired: 18
- Stream gaps logged: 8946

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
