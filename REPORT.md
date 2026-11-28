# Paper bot check-in (2026-11-28 00:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1107 / 188 / 21 | 1100 | 23% | +0.2803 | -0.2153 | **-0.1000** | -109.9472 | 7.912 (top-ups 97.55) | -110.560 | 7 | 0 |
| `m1_random` | 1088 / 121 / 118 | 1085 | 24% | +0.2563 | -0.2123 | **-0.1000** | -108.4941 | 7.637 (top-ups 96.30) | -108.815 | 3 | 0 |

- Exit reasons: {'take_profit': 533, 'stop_loss': 1426, 'no_volume_15m': 225, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 954
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.198, m1_random +6.840
- Circuit breakers fired: 105
- Stream gaps logged: 116911

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 125 / 16 / 0 | 118 | 25% | +0.3205 | -0.2192 | **-0.0820** | -9.6755 | 7.912 (top-ups 97.55) | -11.382 | 7 | 0 |
| `m1_random` | 90 / 11 / 3 | 87 | 18% | +0.3019 | -0.2004 | **-0.1080** | -9.4003 | 7.637 (top-ups 96.30) | -9.291 | 3 | 0 |

- Exit reasons: {'stop_loss': 136, 'take_profit': 45, 'no_volume_15m': 24}
- Sells priced by the verified curve formula because Jupiter had no route: 114
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.312, m1_random +0.213
- Circuit breakers fired: 9
- Stream gaps logged: 12947

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
