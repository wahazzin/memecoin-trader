# Paper bot check-in (2026-11-26 00:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1074 / 185 / 21 | 1072 | 23% | +0.2816 | -0.2156 | **-0.1006** | -107.8397 | 9.426 (top-ups 97.55) | -108.486 | 2 | 0 |
| `m1_random` | 1045 / 113 / 116 | 1042 | 24% | +0.2518 | -0.2121 | **-0.0999** | -104.1175 | 11.838 (top-ups 96.30) | -104.615 | 3 | 1 |

- Exit reasons: {'take_profit': 512, 'stop_loss': 1385, 'no_volume_15m': 216, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 914
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.801
- Circuit breakers fired: 101
- Stream gaps logged: 112615

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 92 / 13 / 0 | 90 | 24% | +0.3499 | -0.2245 | **-0.0841** | -7.5680 | 9.426 (top-ups 97.55) | -9.309 | 2 | 0 |
| `m1_random` | 47 / 3 / 1 | 44 | 18% | +0.2060 | -0.1853 | **-0.1142** | -5.0238 | 11.838 (top-ups 96.30) | -5.090 | 3 | 1 |

- Exit reasons: {'stop_loss': 95, 'take_profit': 24, 'no_volume_15m': 15}
- Sells priced by the verified curve formula because Jupiter had no route: 74
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.174
- Circuit breakers fired: 5
- Stream gaps logged: 8651

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
