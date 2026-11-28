# Paper bot check-in (2026-11-28 00:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1107 / 188 / 21 | 1101 | 23% | +0.2803 | -0.2151 | **-0.0999** | -109.9694 | 6.964 (top-ups 97.55) | -110.948 | 6 | 0 |
| `m1_random` | 1093 / 122 / 118 | 1089 | 24% | +0.2563 | -0.2116 | **-0.0999** | -108.7815 | 7.548 (top-ups 96.30) | -108.904 | 4 | 1 |

- Exit reasons: {'take_profit': 533, 'stop_loss': 1428, 'no_volume_15m': 228, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 958
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.198, m1_random +6.840
- Circuit breakers fired: 105
- Stream gaps logged: 116913

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 125 / 16 / 0 | 119 | 25% | +0.3205 | -0.2170 | **-0.0815** | -9.6977 | 6.964 (top-ups 97.55) | -11.770 | 6 | 0 |
| `m1_random` | 95 / 12 / 3 | 91 | 18% | +0.3019 | -0.1936 | **-0.1065** | -9.6877 | 7.548 (top-ups 96.30) | -9.380 | 4 | 1 |

- Exit reasons: {'stop_loss': 138, 'take_profit': 45, 'no_volume_15m': 27}
- Sells priced by the verified curve formula because Jupiter had no route: 118
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.312, m1_random +0.213
- Circuit breakers fired: 9
- Stream gaps logged: 12949

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
