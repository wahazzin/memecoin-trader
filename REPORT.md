# Paper bot check-in (2026-11-16 03:20 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 760 / 129 / 21 | 760 | 22% | +0.2558 | -0.2203 | **-0.1132** | -86.0010 | 16.946 (top-ups 83.24) | -86.653 | 0 | 0 |
| `m1_random` | 849 / 93 / 112 | 849 | 25% | +0.2574 | -0.2138 | **-0.0978** | -83.0307 | 19.145 (top-ups 82.11) | -83.125 | 0 | 0 |

- Exit reasons: {'take_profit': 406, 'stop_loss': 1048, 'no_volume_15m': 155}
- Sells priced by the verified curve formula because Jupiter had no route: 650
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.350, m1_random +6.055
- Circuit breakers fired: 81
- Stream gaps logged: 89928

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
