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


class TestSmallUploads(unittest.TestCase):
    def test_alerts_only_when_newest_files_are_tiny(self):
        from memebot.health import small_uploads
        normal = [4_000_000 + i * 1000 for i in range(48)]
        self.assertIsNone(small_uploads(normal + [3_900_000, 4_100_000, 4_000_000]))
        self.assertIsNone(small_uploads(normal + [300_000, 4_100_000, 400_000]))     # one normal hour -> fine
        self.assertIn("almost empty", small_uploads(normal + [563_200, 399_360, 174_080]))   # 2026-11-20 shape
        self.assertIsNone(small_uploads([100] * 5))                                    # too little history
