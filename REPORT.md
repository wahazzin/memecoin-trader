# Paper bot check-in (2026-11-16 00:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 753 / 128 / 21 | 752 | 23% | +0.2534 | -0.2204 | **-0.1133** | -85.2141 | 17.911 (top-ups 83.24) | -85.689 | 1 | 0 |
| `m1_random` | 841 / 91 / 112 | 841 | 25% | +0.2572 | -0.2129 | **-0.0972** | -81.7514 | 20.133 (top-ups 82.11) | -82.273 | 0 | 0 |

- Exit reasons: {'take_profit': 403, 'stop_loss': 1038, 'no_volume_15m': 152}
- Sells priced by the verified curve formula because Jupiter had no route: 642
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.301, m1_random +6.022
- Circuit breakers fired: 80
- Stream gaps logged: 89510

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
