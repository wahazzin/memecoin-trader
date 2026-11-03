# Paper bot check-in (2026-11-03 01:54 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 553 / 84 / 15 | 553 | 23% | +0.2677 | -0.2178 | **-0.1054** | -58.2920 | 15.700 (top-ups 54.23) | -59.093 | 0 | 0 |
| `m1_random` | 529 / 56 / 57 | 529 | 23% | +0.2585 | -0.2186 | **-0.1095** | -57.9124 | 15.910 (top-ups 53.97) | -58.218 | 0 | 0 |

- Exit reasons: {'take_profit': 268, 'stop_loss': 717, 'no_volume_15m': 97}
- Sells priced by the verified curve formula because Jupiter had no route: 393
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65880

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
