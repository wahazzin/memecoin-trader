# Paper bot check-in (2026-11-28 00:06 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1101 / 188 / 21 | 1094 | 23% | +0.2793 | -0.2148 | **-0.1001** | -109.4974 | 7.352 (top-ups 97.55) | -110.560 | 7 | 0 |
| `m1_random` | 1085 / 120 / 118 | 1082 | 24% | +0.2557 | -0.2122 | **-0.1002** | -108.4065 | 8.098 (top-ups 96.30) | -108.354 | 3 | 0 |

- Exit reasons: {'take_profit': 530, 'stop_loss': 1420, 'no_volume_15m': 225, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 950
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.178, m1_random +6.840
- Circuit breakers fired: 104
- Stream gaps logged: 116906

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 119 / 16 / 0 | 112 | 25% | +0.3143 | -0.2146 | **-0.0824** | -9.2258 | 7.352 (top-ups 97.55) | -11.382 | 7 | 0 |
| `m1_random` | 87 / 10 / 3 | 84 | 18% | +0.2953 | -0.1992 | **-0.1109** | -9.3127 | 8.098 (top-ups 96.30) | -8.830 | 3 | 0 |

- Exit reasons: {'stop_loss': 130, 'take_profit': 42, 'no_volume_15m': 24}
- Sells priced by the verified curve formula because Jupiter had no route: 110
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.292, m1_random +0.213
- Circuit breakers fired: 8
- Stream gaps logged: 12942

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
