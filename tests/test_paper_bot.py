import os
import sys
import tempfile
import time
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from memebot import paper, bot  # noqa: E402

NOSLEEP = lambda s: None


def fake_quotes(*outs):
    it = iter(outs)
    def q(inp, outp, amount):
        o = next(it)
        return {"error": "NO_ROUTES_FOUND", "t": 0} if o is None else {"out": o, "impact": 0, "route": ["Pump.fun"], "t": 0}
    return q


class TestPaper(unittest.TestCase):
    def setUp(self):
        self.orig = paper.quote

    def tearDown(self):
        paper.quote = self.orig

    def test_buy_fills_at_worse_quote_and_adds_measured_costs(self):
        paper.quote = fake_quotes(1_000_000_000, 950_000_000)       # tokens (raw, 6 decimals)
        r = paper.buy("M", 0.5, first_buy=True, sleep=NOSLEEP)
        self.assertEqual(r["status"], "FILLED")
        self.assertAlmostEqual(r["tokens"], 950.0)                   # the worse one
        self.assertAlmostEqual(r["cost_sol"], 0.5 + paper.PRIORITY_SOL + paper.NETWORK_SOL + paper.RENT_SOL)

    def test_buy_fails_past_slippage_but_pays_fees(self):
        paper.quote = fake_quotes(1_000_000_000, 700_000_000)        # 30% worse > 20% slippage
        r = paper.buy("M", 0.5, sleep=NOSLEEP)
        self.assertEqual(r["status"], "FAILED")
        self.assertAlmostEqual(r["cost_sol"], paper.PRIORITY_SOL + paper.NETWORK_SOL)

    def test_no_route(self):
        paper.quote = fake_quotes(None, None)
        self.assertEqual(paper.buy("M", 0.5, sleep=NOSLEEP)["status"], "NO_ROUTE")

    def test_sell_refunds_rent_and_takes_worse_quote(self):
        paper.quote = fake_quotes(600_000_000, 550_000_000)          # lamports
        r = paper.sell("M", 950.0, sleep=NOSLEEP)
        self.assertAlmostEqual(r["proceeds_sol"], 0.55 - paper.PRIORITY_SOL - paper.NETWORK_SOL + paper.RENT_SOL)


class TestBot(unittest.TestCase):
    def make(self):
        return bot.Bot(bot.State(tempfile.mkdtemp()))

    def trade(self, mint, ts, user, buy, sol, vsol, vtok=1.0e9, tok=1e6):
        return {"mint": mint, "ts": ts, "user": user, "buy": buy, "sol": sol, "tok": tok, "vsol": vsol, "vtok": vtok,
                "cfee_bps": 30, "fee_bps": 95}

    def test_checkpoint_signal_at_2_5x_launch(self):
        b = self.make()
        now = time.time()
        b.on_create({"mint": "M", "traderPublicKey": "dev"})
        b.coins["M"]["created"] = now
        self.assertIsNone(b.on_trade(self.trade("M", now + 1, "dev", True, 0.2, 30.0)))
        self.assertIsNone(b.on_trade(self.trade("M", now + 5, "a", True, 1.0, 40.0)))
        sig = b.on_trade(self.trade("M", now + 9, "b", True, 1.0, 76.0))   # price 2.53x launch
        self.assertIsNotNone(sig)
        self.assertIn("C1", sig["checks"])
        self.assertIsNone(b.on_trade(self.trade("M", now + 12, "c", True, 1.0, 80.0)))   # judged once

    def test_too_old_coins_are_never_signalled(self):
        b = self.make()
        now = time.time()
        b.on_create({"mint": "M", "traderPublicKey": "dev"})
        b.coins["M"]["created"] = now - 3000
        b.on_trade(self.trade("M", now - 2990, "dev", True, 0.2, 30.0))
        self.assertIsNone(b.on_trade(self.trade("M", now, "b", True, 1.0, 80.0)))

    def test_exit_rules(self):
        b = self.make()
        now = time.time()
        p = {"entry_price": 1.0, "opened": now - 10}
        b.price["M"], b.last_trade["M"] = 1.6, now
        self.assertEqual(b.exit_reason(p, "M", now), "take_profit")
        b.price["M"] = 0.79
        self.assertEqual(b.exit_reason(p, "M", now), "stop_loss")
        b.price["M"], b.last_trade["M"] = 1.0, now - 901
        self.assertEqual(b.exit_reason(p, "M", now), "no_volume_15m")
        b.last_trade["M"] = now
        self.assertEqual(b.exit_reason({"entry_price": 1.0, "opened": now - 3601}, "M", now), "max_hold_60m")
        self.assertIsNone(b.exit_reason(p, "M", now))

    def test_circuit_breaker_halts_arm(self):
        b = self.make()
        self.assertTrue(b.day_ok("m1_pass"))
        b.s.cash["m1_pass"] = 20.0 * (1 - bot.DAILY_LOSS_LIMIT) - 0.01
        self.assertFalse(b.day_ok("m1_pass"))
        self.assertFalse(b.day_ok("m1_pass"))                      # stays halted the rest of the day

    def test_bot_has_no_signing_code(self):
        src = open(bot.__file__).read() + open(paper.__file__).read()
        for bad in ("sendTransaction", "private_key", "Keypair", "secret_key", "/swap/v1/swap"):
            self.assertNotIn(bad, src)


if __name__ == "__main__":
    unittest.main()


class TestFallback(unittest.TestCase):
    def test_no_route_sell_uses_curve_formula_only_when_curve_is_live(self):
        orig = paper.quote
        try:
            paper.quote = fake_quotes(None, None)
            r = paper.sell("M", 1_000_000, sleep=NOSLEEP, curve_now=lambda: (40.0, 8e8, 0.0125, 5))
            self.assertEqual((r["status"], r["source"]), ("FILLED", "curve_formula"))
            self.assertGreater(r["proceeds_sol"], 0)
            paper.quote = fake_quotes(None, None)
            r = paper.sell("M", 1_000_000, sleep=NOSLEEP, curve_now=lambda: (40.0, 8e8, 0.0125, 300))
            self.assertEqual(r["status"], "NO_ROUTE")                 # stale curve: stays stuck
        finally:
            paper.quote = orig


class TestCurveAddress(unittest.TestCase):
    def test_derived_curve_matches_known_coin(self):
        self.assertEqual(bot.curve_address("BuMa6muvh95x24wMQVyoi3hGpMHctNhXFEommnsmxjAe"),
                         "F1nLwiMEsn8U6oqK1wbjRpEi7Y93XGy42wXFYzDc5pum")
