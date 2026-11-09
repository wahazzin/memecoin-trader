"""tail_text must not use suffix ranges (raw.githubusercontent answers 'bytes=-N' with 501 since 2026-11-06)."""
import unittest

import requests

from memebot.health import tail_text


class _R:
    def __init__(self, code, text="", headers=None):
        self.status_code, self.text, self.headers = code, text, headers or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(str(self.status_code))


BODY = "".join('{"ts": %d}\n' % i for i in range(1000))


def fake_get(url, headers=None, **kw):
    rng = (headers or {}).get("Range")
    if rng is None:
        return _R(200, BODY)
    start, end = rng.split("=")[1].split("-")
    if start == "":
        return _R(501)                       # what raw.githubusercontent does now
    return _R(206, BODY[int(start):])


def fake_head(url, **kw):
    return _R(200, headers={"Content-Length": str(len(BODY))})


class TestTail(unittest.TestCase):
    def test_tail_uses_explicit_range(self):
        t = tail_text("u", 100, head=fake_head, get=fake_get)
        self.assertEqual(len(t), 100)
        self.assertTrue(t.endswith('{"ts": 999}\n'))

    def test_small_file_read_whole(self):
        self.assertEqual(tail_text("u", 10 ** 9, head=fake_head, get=fake_get), BODY)


if __name__ == "__main__":
    unittest.main()
