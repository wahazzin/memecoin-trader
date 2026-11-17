# Paper bot check-in (2026-11-17 00:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 774 / 131 / 21 | 773 | 23% | +0.2613 | -0.2201 | **-0.1111** | -85.8910 | 17.486 (top-ups 83.24) | -86.842 | 1 | 0 |
| `m1_random` | 869 / 97 / 112 | 868 | 25% | +0.2571 | -0.2146 | **-0.0983** | -85.3097 | 16.561 (top-ups 82.11) | -85.708 | 1 | 0 |

- Exit reasons: {'take_profit': 413, 'stop_loss': 1072, 'no_volume_15m': 156}
- Sells priced by the verified curve formula because Jupiter had no route: 663
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.371, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 91979

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
