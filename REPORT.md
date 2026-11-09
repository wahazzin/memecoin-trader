# Paper bot check-in (2026-11-09 04:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 647 / 104 / 17 | 647 | 23% | +0.2601 | -0.2179 | **-0.1085** | -70.2303 | 18.074 (top-ups 68.54) | -71.117 | 0 | 0 |
| `m1_random` | 693 / 80 / 92 | 693 | 24% | +0.2517 | -0.2101 | **-0.0988** | -68.4768 | 19.354 (top-ups 68.02) | -68.826 | 0 | 0 |

- Exit reasons: {'take_profit': 327, 'stop_loss': 879, 'no_volume_15m': 134}
- Sells priced by the verified curve formula because Jupiter had no route: 527
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.831
- Circuit breakers fired: 66
- Stream gaps logged: 77465

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
