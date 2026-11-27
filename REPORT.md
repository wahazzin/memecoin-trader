# Paper bot check-in (2026-11-27 00:05 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1083 / 186 / 21 | 1082 | 23% | +0.2812 | -0.2150 | **-0.1008** | -109.0762 | 8.735 (top-ups 97.55) | -109.177 | 1 | 0 |
| `m1_random` | 1064 / 116 / 118 | 1063 | 24% | +0.2538 | -0.2110 | **-0.0991** | -105.3461 | 10.431 (top-ups 96.30) | -106.302 | 1 | 0 |

- Exit reasons: {'take_profit': 521, 'stop_loss': 1400, 'no_volume_15m': 223, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 934
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.839
- Circuit breakers fired: 103
- Stream gaps logged: 115303

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 101 / 14 / 0 | 100 | 23% | +0.3422 | -0.2166 | **-0.0880** | -8.8045 | 8.735 (top-ups 97.55) | -9.999 | 1 | 0 |
| `m1_random` | 66 / 6 / 3 | 65 | 18% | +0.2637 | -0.1777 | **-0.0962** | -6.2523 | 10.431 (top-ups 96.30) | -6.778 | 1 | 0 |

- Exit reasons: {'stop_loss': 110, 'take_profit': 33, 'no_volume_15m': 22}
- Sells priced by the verified curve formula because Jupiter had no route: 94
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.212
- Circuit breakers fired: 7
- Stream gaps logged: 11339

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
