# Paper bot check-in (2026-11-19 01:16 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 856 / 151 / 21 | 854 | 23% | +0.2720 | -0.2168 | **-0.1063** | -90.7961 | 19.374 (top-ups 83.24) | -92.852 | 2 | 0 |
| `m1_random` | 929 / 106 / 114 | 928 | 25% | +0.2538 | -0.2134 | **-0.0971** | -90.1467 | 11.670 (top-ups 82.11) | -91.184 | 1 | 0 |

- Exit reasons: {'take_profit': 444, 'stop_loss': 1166, 'no_volume_15m': 172}
- Sells priced by the verified curve formula because Jupiter had no route: 745
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.518, m1_random +6.383
- Circuit breakers fired: 86
- Stream gaps logged: 95093

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
