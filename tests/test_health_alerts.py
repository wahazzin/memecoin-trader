"""Alert repeat intervals (2026-11-02): storage warning weekly, outages every 6 h."""
import unittest

from memebot.health import alert_due


class TestAlertDue(unittest.TestCase):
    def test_storage_repeats_weekly_not_every_6h(self):
        now = 10_000_000.0
        self.assertTrue(alert_due("storage", {}, now))
        self.assertFalse(alert_due("storage", {"storage": now - 7 * 3600}, now))
        self.assertFalse(alert_due("storage", {"storage": now - 6 * 86400}, now))
        self.assertTrue(alert_due("storage", {"storage": now - 7 * 86400 - 1}, now))

    def test_outages_still_repeat_every_6h(self):
        now = 10_000_000.0
        self.assertTrue(alert_due("recorder", {"recorder": now - 6 * 3600 - 1}, now))
        self.assertFalse(alert_due("recorder", {"recorder": now - 3600}, now))


if __name__ == "__main__":
    unittest.main()
