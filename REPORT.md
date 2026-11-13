# Paper bot check-in (2026-11-13 01:02 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 715 / 121 / 21 | 714 | 22% | +0.2559 | -0.2190 | **-0.1126** | -80.3881 | 7.862 (top-ups 68.54) | -81.044 | 1 | 0 |
| `m1_random` | 805 / 89 / 111 | 805 | 25% | +0.2596 | -0.2138 | **-0.0968** | -77.9086 | 9.892 (top-ups 68.02) | -78.288 | 0 | 0 |

- Exit reasons: {'take_profit': 377, 'stop_loss': 995, 'no_volume_15m': 147}
- Sells priced by the verified curve formula because Jupiter had no route: 612
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.597
- Circuit breakers fired: 75
- Stream gaps logged: 84712

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
