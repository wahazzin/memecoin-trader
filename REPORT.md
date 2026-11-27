# Paper bot check-in (2026-11-27 00:15 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1083 / 186 / 21 | 1082 | 23% | +0.2812 | -0.2150 | **-0.1008** | -109.0762 | 8.013 (top-ups 97.55) | -109.899 | 1 | 0 |
| `m1_random` | 1070 / 118 / 118 | 1069 | 24% | +0.2557 | -0.2109 | **-0.0979** | -104.6416 | 11.338 (top-ups 96.30) | -106.302 | 1 | 0 |

- Exit reasons: {'take_profit': 524, 'stop_loss': 1403, 'no_volume_15m': 223, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 937
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.839
- Circuit breakers fired: 103
- Stream gaps logged: 115312

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 101 / 14 / 0 | 100 | 23% | +0.3422 | -0.2166 | **-0.0880** | -8.8045 | 8.013 (top-ups 97.55) | -10.722 | 1 | 0 |
| `m1_random` | 72 / 8 / 3 | 71 | 21% | +0.2953 | -0.1782 | **-0.0781** | -5.5479 | 11.338 (top-ups 96.30) | -6.778 | 1 | 0 |

- Exit reasons: {'stop_loss': 113, 'take_profit': 36, 'no_volume_15m': 22}
- Sells priced by the verified curve formula because Jupiter had no route: 97
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.212
- Circuit breakers fired: 7
- Stream gaps logged: 11348

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
