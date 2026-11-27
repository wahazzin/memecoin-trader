# Paper bot check-in (2026-11-27 00:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1083 / 186 / 21 | 1083 | 23% | +0.2812 | -0.2148 | **-0.1007** | -109.1003 | 8.015 (top-ups 97.55) | -109.899 | 0 | 0 |
| `m1_random` | 1076 / 119 / 118 | 1075 | 24% | +0.2557 | -0.2120 | **-0.0993** | -106.7740 | 10.190 (top-ups 96.30) | -106.302 | 1 | 0 |

- Exit reasons: {'take_profit': 525, 'stop_loss': 1408, 'no_volume_15m': 224, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 939
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.840
- Circuit breakers fired: 103
- Stream gaps logged: 115316

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 101 / 14 / 0 | 101 | 23% | +0.3422 | -0.2141 | **-0.0874** | -8.8286 | 8.015 (top-ups 97.55) | -10.722 | 0 | 0 |
| `m1_random` | 78 / 9 / 3 | 77 | 19% | +0.2953 | -0.1953 | **-0.0997** | -7.6802 | 10.190 (top-ups 96.30) | -6.778 | 1 | 0 |

- Exit reasons: {'stop_loss': 118, 'take_profit': 37, 'no_volume_15m': 23}
- Sells priced by the verified curve formula because Jupiter had no route: 99
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.213
- Circuit breakers fired: 7
- Stream gaps logged: 11352

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
