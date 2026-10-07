"""Minimal base58 encoder (Bitcoin alphabet), so the probe has no extra dependency."""
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def encode(b):
    n = int.from_bytes(b, "big")
    s = ""
    while n:
        n, r = divmod(n, 58)
        s = ALPHABET[r] + s
    pad = len(b) - len(b.lstrip(b"\0"))
    return "1" * pad + s
