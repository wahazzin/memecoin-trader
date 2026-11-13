# Paper bot check-in (2026-11-13 00:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 712 / 120 / 21 | 710 | 23% | +0.2559 | -0.2179 | **-0.1111** | -78.8803 | 9.371 (top-ups 68.54) | -79.612 | 2 | 0 |
| `m1_random` | 805 / 89 / 111 | 804 | 25% | +0.2596 | -0.2141 | **-0.0968** | -77.8654 | 9.892 (top-ups 68.02) | -78.288 | 1 | 0 |

- Exit reasons: {'take_profit': 377, 'stop_loss': 991, 'no_volume_15m': 146}
- Sells priced by the verified curve formula because Jupiter had no route: 610
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.597
- Circuit breakers fired: 74
- Stream gaps logged: 84663

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
