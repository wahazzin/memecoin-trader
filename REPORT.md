# Paper bot check-in (2026-11-25 00:39 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1064 / 184 / 21 | 1064 | 23% | +0.2816 | -0.2151 | **-0.0993** | -105.6922 | 11.428 (top-ups 97.55) | -106.484 | 0 | 0 |
| `m1_random` | 1034 / 113 / 116 | 1034 | 24% | +0.2526 | -0.2124 | **-0.0995** | -102.8811 | 12.455 (top-ups 96.30) | -103.998 | 0 | 0 |

- Exit reasons: {'take_profit': 509, 'stop_loss': 1372, 'no_volume_15m': 216, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 905
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.142, m1_random +6.801
- Circuit breakers fired: 99
- Stream gaps logged: 109063

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 82 / 12 / 0 | 82 | 27% | +0.3499 | -0.2186 | **-0.0661** | -5.4205 | 11.428 (top-ups 97.55) | -7.307 | 0 | 0 |
| `m1_random` | 36 / 3 / 1 | 36 | 19% | +0.2306 | -0.1863 | **-0.1052** | -3.7873 | 12.455 (top-ups 96.30) | -4.474 | 0 | 0 |

- Exit reasons: {'stop_loss': 82, 'take_profit': 21, 'no_volume_15m': 15}
- Sells priced by the verified curve formula because Jupiter had no route: 65
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.256, m1_random +0.174
- Circuit breakers fired: 3
- Stream gaps logged: 5099

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
