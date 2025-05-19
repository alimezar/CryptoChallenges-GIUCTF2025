#!/usr/bin/env python3
import base64, itertools

cipher_b64 = "rb2Nuri44cdr6Nml1Ndr1rGm2uhr6dfRu+ed1rjamdN+6ZjZ06em69fv"
cipher     = base64.b64decode(cipher_b64)

fragments = ["R3boot", "Dr4g0n", "Ech0", "L1ght", "S1gn4l"]

digits = "0123456789abcdefghijklmnopqrstuvwxyz"
def to_base36(n: int) -> str:
    if n == 0: return "0"
    out = ""
    while n:
        n, r = divmod(n, 36)
        out = digits[r] + out
    return out

def ascii_sum(s: str) -> int:
    return sum(map(ord, s))

for combo in itertools.permutations(fragments, 3):
    key = "".join(to_base36(ascii_sum(f)) for f in combo).encode()

    plain = bytes((c - key[i % len(key)]) % 256 for i, c in enumerate(cipher))
    try:
        text = plain.decode("utf-8")
    except UnicodeDecodeError:
        continue

    if text.startswith("GIUCTF{"):
        print("Fragments order :", combo)
        print("Derived key     :", key.decode())
        print("Decrypted flag  :", text)
        break
