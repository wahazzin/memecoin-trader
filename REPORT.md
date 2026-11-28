# Paper bot check-in (2026-11-28 00:01 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1085 / 186 / 21 | 1084 | 23% | +0.2812 | -0.2147 | **-0.1008** | -109.2269 | 8.015 (top-ups 97.55) | -109.899 | 1 | 0 |
| `m1_random` | 1081 / 119 / 118 | 1080 | 24% | +0.2557 | -0.2120 | **-0.0998** | -107.8291 | 8.354 (top-ups 96.30) | -108.098 | 1 | 0 |

- Exit reasons: {'take_profit': 527, 'stop_loss': 1411, 'no_volume_15m': 225, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 942
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.840
- Circuit breakers fired: 104
- Stream gaps logged: 116906

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 103 / 14 / 0 | 102 | 23% | +0.3422 | -0.2130 | **-0.0878** | -8.9552 | 8.015 (top-ups 97.55) | -10.722 | 1 | 0 |
| `m1_random` | 83 / 9 / 3 | 82 | 18% | +0.2953 | -0.1965 | **-0.1065** | -8.7353 | 8.354 (top-ups 96.30) | -8.574 | 1 | 0 |

- Exit reasons: {'stop_loss': 121, 'take_profit': 39, 'no_volume_15m': 24}
- Sells priced by the verified curve formula because Jupiter had no route: 102
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.213
- Circuit breakers fired: 8
- Stream gaps logged: 12942

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
