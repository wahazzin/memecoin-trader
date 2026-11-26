# Paper bot check-in (2026-11-26 00:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1072 / 185 / 21 | 1070 | 23% | +0.2816 | -0.2154 | **-0.1002** | -107.1969 | 10.376 (top-ups 97.55) | -107.536 | 2 | 0 |
| `m1_random` | 1040 / 113 / 116 | 1040 | 24% | +0.2518 | -0.2126 | **-0.1001** | -104.0677 | 11.947 (top-ups 96.30) | -104.506 | 0 | 0 |

- Exit reasons: {'take_profit': 511, 'stop_loss': 1382, 'no_volume_15m': 216, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 911
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.801
- Circuit breakers fired: 100
- Stream gaps logged: 112593

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 90 / 13 / 0 | 88 | 25% | +0.3499 | -0.2216 | **-0.0787** | -6.9252 | 10.376 (top-ups 97.55) | -8.359 | 2 | 0 |
| `m1_random` | 42 / 3 / 1 | 42 | 19% | +0.2060 | -0.1948 | **-0.1184** | -4.9739 | 11.947 (top-ups 96.30) | -4.981 | 0 | 0 |

- Exit reasons: {'stop_loss': 92, 'take_profit': 23, 'no_volume_15m': 15}
- Sells priced by the verified curve formula because Jupiter had no route: 71
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.174
- Circuit breakers fired: 4
- Stream gaps logged: 8629

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
