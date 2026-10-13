import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research import w1  # noqa: E402


class TestW1(unittest.TestCase):
    def test_planted_skill_passes_and_no_skill_does_not(self):
        _, a, b = w1.run(w1.synthetic(True), boot=300)
        self.assertTrue(a and b)
        _, a, b = w1.run(w1.synthetic(False), boot=300)
        self.assertFalse(a or b)

    def test_creator_positions_are_dropped(self):
        c = {"mint": "M", "creator": "dev", "trades": [
            {"ts": 1, "user": "dev", "buy": True, "sol": 1, "tok": 10, "vsol": 31, "vtok": 1e9, "fee": 0.01, "cfee": 0.003},
            {"ts": 2, "user": "a", "buy": True, "sol": 1, "tok": 10, "vsol": 32, "vtok": 1e9, "fee": 0.01, "cfee": 0.003}]}
        self.assertEqual([p["wallet"] for p in w1.positions([c])], ["a"])

    def test_wallet_pnl_includes_event_fees(self):
        c = {"mint": "M", "creator": "dev", "trades": [
            {"ts": 1, "user": "a", "buy": True, "sol": 1.0, "tok": 10, "vsol": 31, "vtok": 1e9, "fee": 0.0095, "cfee": 0.003},
            {"ts": 2, "user": "a", "buy": False, "sol": 1.0, "tok": 10, "vsol": 30, "vtok": 1e9, "fee": 0.0095, "cfee": 0.003}]}
        p = w1.positions([c])[0]
        self.assertTrue(p["closed"])
        self.assertAlmostEqual(p["pnl"], -0.025)


if __name__ == "__main__":
    unittest.main()
