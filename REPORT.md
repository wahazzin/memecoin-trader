# Paper bot check-in (2026-11-19 01:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 851 / 151 / 21 | 850 | 23% | +0.2692 | -0.2166 | **-0.1069** | -90.8480 | 18.736 (top-ups 83.24) | -92.852 | 1 | 0 |
| `m1_random` | 928 / 106 / 114 | 927 | 25% | +0.2525 | -0.2134 | **-0.0978** | -90.6813 | 11.135 (top-ups 82.11) | -91.184 | 1 | 0 |

- Exit reasons: {'take_profit': 442, 'stop_loss': 1163, 'no_volume_15m': 172}
- Sells priced by the verified curve formula because Jupiter had no route: 740
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.518, m1_random +6.383
- Circuit breakers fired: 86
- Stream gaps logged: 95090

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
