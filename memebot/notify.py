"""Discord alerts. The webhook lives ONLY in the GitHub secret DISCORD_WEBHOOK_URL (never in code or files).
Without it, alerts are printed instead (nothing breaks)."""
import os
import sys

import requests


def send(msg):
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    msg = msg[:1900]
    if not url:
        print("[alert, no webhook set]", msg)
        return False
    try:
        r = requests.post(url, json={"content": msg}, timeout=15)
        return r.status_code in (200, 204)
    except Exception as e:
        print("discord failed:", type(e).__name__)
        return False


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or sys.stdin.read()
    ok = send(text)
    print("sent" if ok else "not sent")
