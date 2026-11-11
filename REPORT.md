# Paper bot check-in (2026-11-11 00:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 677 / 111 / 19 | 677 | 22% | +0.2613 | -0.2195 | **-0.1116** | -75.5434 | 12.745 (top-ups 68.54) | -76.161 | 0 | 0 |
| `m1_random` | 738 / 85 / 102 | 738 | 24% | +0.2502 | -0.2118 | **-0.0998** | -73.6316 | 14.184 (top-ups 68.02) | -73.996 | 0 | 0 |

- Exit reasons: {'take_profit': 349, 'stop_loss': 925, 'no_volume_15m': 141}
- Sells priced by the verified curve formula because Jupiter had no route: 568
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +4.994
- Circuit breakers fired: 70
- Stream gaps logged: 80796

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
