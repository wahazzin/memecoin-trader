# Paper bot check-in (2026-11-06 00:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 595 / 95 / 16 | 593 | 22% | +0.2693 | -0.2192 | **-0.1096** | -65.0118 | 8.496 (top-ups 54.23) | -66.099 | 2 | 0 |
| `m1_random` | 656 / 73 / 81 | 656 | 25% | +0.2550 | -0.2117 | **-0.0972** | -63.7421 | 10.050 (top-ups 53.97) | -64.080 | 0 | 0 |

- Exit reasons: {'take_profit': 311, 'stop_loss': 818, 'no_volume_15m': 120}
- Sells priced by the verified curve formula because Jupiter had no route: 472
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.706
- Circuit breakers fired: 60
- Stream gaps logged: 74070

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
