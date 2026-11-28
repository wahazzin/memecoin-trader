# Paper bot check-in (2026-11-28 00:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1107 / 188 / 21 | 1105 | 23% | +0.2803 | -0.2144 | **-0.0997** | -110.2200 | 6.969 (top-ups 97.55) | -110.948 | 2 | 0 |
| `m1_random` | 1098 / 122 / 118 | 1094 | 24% | +0.2578 | -0.2116 | **-0.0987** | -108.0284 | 7.736 (top-ups 96.30) | -108.904 | 4 | 0 |

- Exit reasons: {'take_profit': 535, 'stop_loss': 1431, 'no_volume_15m': 232, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 963
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.198, m1_random +7.031
- Circuit breakers fired: 105
- Stream gaps logged: 116913

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 125 / 16 / 0 | 123 | 24% | +0.3205 | -0.2104 | **-0.0809** | -9.9484 | 6.969 (top-ups 97.55) | -11.770 | 2 | 0 |
| `m1_random` | 100 / 12 / 3 | 96 | 20% | +0.3162 | -0.1941 | **-0.0931** | -8.9346 | 7.736 (top-ups 96.30) | -9.380 | 4 | 0 |

- Exit reasons: {'stop_loss': 141, 'take_profit': 47, 'no_volume_15m': 31}
- Sells priced by the verified curve formula because Jupiter had no route: 123
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.312, m1_random +0.404
- Circuit breakers fired: 9
- Stream gaps logged: 12949

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
