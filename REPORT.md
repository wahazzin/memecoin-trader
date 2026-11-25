# Paper bot check-in (2026-11-25 00:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1064 / 184 / 21 | 1063 | 23% | +0.2816 | -0.2152 | **-0.0993** | -105.5063 | 13.081 (top-ups 97.55) | -104.831 | 1 | 0 |
| `m1_random` | 1028 / 113 / 116 | 1028 | 24% | +0.2530 | -0.2124 | **-0.1001** | -102.9091 | 13.105 (top-ups 96.30) | -103.347 | 0 | 0 |

- Exit reasons: {'take_profit': 507, 'stop_loss': 1369, 'no_volume_15m': 214, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 902
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.142, m1_random +6.719
- Circuit breakers fired: 99
- Stream gaps logged: 108989

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 82 / 12 / 0 | 81 | 27% | +0.3499 | -0.2192 | **-0.0646** | -5.2346 | 13.081 (top-ups 97.55) | -5.653 | 1 | 0 |
| `m1_random` | 30 / 3 / 1 | 30 | 13% | +0.2343 | -0.1828 | **-0.1272** | -3.8153 | 13.105 (top-ups 96.30) | -3.823 | 0 | 0 |

- Exit reasons: {'stop_loss': 79, 'take_profit': 19, 'no_volume_15m': 13}
- Sells priced by the verified curve formula because Jupiter had no route: 62
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.256, m1_random +0.092
- Circuit breakers fired: 3
- Stream gaps logged: 5025

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
