# Paper bot check-in (2026-11-23 01:48 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 943 / 167 / 21 | 943 | 23% | +0.2738 | -0.2158 | **-0.1052** | -99.2214 | 17.944 (top-ups 97.55) | -99.969 | 0 | 0 |
| `m1_random` | 980 / 109 / 114 | 980 | 24% | +0.2545 | -0.2134 | **-0.0988** | -96.8489 | 19.176 (top-ups 96.30) | -97.276 | 0 | 0 |

- Exit reasons: {'take_profit': 470, 'stop_loss': 1258, 'no_volume_15m': 194, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 819
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.753, m1_random +6.598
- Circuit breakers fired: 94
- Stream gaps logged: 102029

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
