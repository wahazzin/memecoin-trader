"""recorder.yml: a failed hour upload must not end the job (2026-11-05: one HTTP 404 killed the recorder, 3 h lost)."""
import os
import subprocess
import tempfile
import unittest

import yaml

WF = os.path.join(os.path.dirname(__file__), "..", ".github", "workflows", "recorder.yml")


def upload_fn():
    y = yaml.safe_load(open(WF))
    run = [s for s in y["jobs"]["record"]["steps"] if s.get("name") == "Record + upload finished hours"][0]["run"]
    return run[run.index("upload() {"):run.index("python -m memebot.recorder")]


class TestUpload(unittest.TestCase):
    def _run(self, gh_rc):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "data", "2026-11-05", "15"))
            open(os.path.join(d, "data", "2026-11-05", "15", "a"), "w").write("x")
            script = (f'gh(){{ [ "$1" = release ] && [ "$2" = upload ] && return {gh_rc}; return 0; }}\n'
                      "REPO=x; GITHUB_RUN_ID=1\n" + upload_fn() +
                      'for h in data/*/*; do [ -d "$h" ] && upload "$h"; done\necho ALIVE\n')
            r = subprocess.run(["bash", "-e", "-c", script], cwd=d, capture_output=True, text=True)
            return r, os.path.isdir(os.path.join(d, "data", "2026-11-05", "15")), [f for f in os.listdir(d) if f.endswith(".tar")]

    def test_failed_upload_keeps_hour_and_job_alive(self):
        r, kept, tars = self._run(1)
        self.assertIn("ALIVE", r.stdout)
        self.assertTrue(kept)
        self.assertEqual(tars, [])

    def test_successful_upload_removes_hour(self):
        r, kept, tars = self._run(0)
        self.assertIn("ALIVE", r.stdout)
        self.assertFalse(kept)
        self.assertEqual(tars, [])


if __name__ == "__main__":
    unittest.main()
