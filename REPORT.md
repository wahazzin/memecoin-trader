# Paper bot check-in (2026-11-28 16:08 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1107 / 188 / 21 | 1107 | 23% | +0.2797 | -0.2141 | **-0.0995** | -110.1336 | 6.979 (top-ups 97.55) | -110.948 | 0 | 0 |
| `m1_random` | 1102 / 122 / 118 | 1102 | 24% | +0.2569 | -0.2115 | **-0.0989** | -108.9717 | 7.025 (top-ups 96.30) | -109.428 | 0 | 0 |

- Exit reasons: {'take_profit': 535, 'stop_loss': 1436, 'no_volume_15m': 237, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 969
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.198, m1_random +7.042
- Circuit breakers fired: 106
- Stream gaps logged: 118891

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 125 / 16 / 0 | 125 | 25% | +0.3136 | -0.2083 | **-0.0789** | -9.8619 | 6.979 (top-ups 97.55) | -11.770 | 0 | 0 |
| `m1_random` | 104 / 12 / 3 | 104 | 20% | +0.2988 | -0.1946 | **-0.0950** | -9.8780 | 7.025 (top-ups 96.30) | -9.904 | 0 | 0 |

- Exit reasons: {'stop_loss': 146, 'take_profit': 47, 'no_volume_15m': 36}
- Sells priced by the verified curve formula because Jupiter had no route: 129
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.312, m1_random +0.415
- Circuit breakers fired: 10
- Stream gaps logged: 14927

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
