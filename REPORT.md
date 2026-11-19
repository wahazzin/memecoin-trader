# Paper bot check-in (2026-11-19 01:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 857 / 152 / 21 | 855 | 23% | +0.2720 | -0.2166 | **-0.1063** | -90.9147 | 11.929 (top-ups 83.24) | -92.852 | 2 | 0 |
| `m1_random` | 929 / 106 / 114 | 929 | 25% | +0.2538 | -0.2132 | **-0.0971** | -90.1778 | 11.672 (top-ups 82.11) | -91.184 | 0 | 0 |

- Exit reasons: {'take_profit': 444, 'stop_loss': 1166, 'no_volume_15m': 174}
- Sells priced by the verified curve formula because Jupiter had no route: 747
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.518, m1_random +6.383
- Circuit breakers fired: 86
- Stream gaps logged: 95096

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
