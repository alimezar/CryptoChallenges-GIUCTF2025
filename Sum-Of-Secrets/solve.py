#!/usr/bin/env python3
import math
from binascii import unhexlify

# RSA public parameters (N, e) and leaked S = p + q
N = int("759f96d1e6d31afe59901283da8040190f3fc0904f744560a54ca8eb215cdb17", 16)
S = int("01657f6c1ccbe7db265e45ace1fdffa778", 16)
e = 65537

# === Step 1: Solve for p and q using S and N ===
# Use quadratic relationship: x^2 - Sx + N = 0
sqrtD = math.isqrt(S*S - 4*N)      # perfect square root of the discriminant
p = (S + sqrtD)//2
q = (S - sqrtD)//2

# === Step 2: Compute RSA private key (d) ===
phi = (p - 1) * (q - 1)
d   = pow(e, -1, phi)              # modular inverse of e modulo phi

# === Step 3: Read ciphertext and decrypt with RSA private key ===
C = int.from_bytes(open("ciphertext.bin", "rb").read(), "big")
m = pow(C, d, N)

# === Step 4: Convert decrypted int back to bytes ===
k = (N.bit_length() + 7) // 8      # byte length of N
plain = m.to_bytes(k, "big")

# === Step 5: Reverse the plaintext ===
rev = plain[::-1]

# === Step 6: Build key from hex(p) as ASCII string ===
key = bytes(hex(p)[2:], "ascii")   # key = ASCII encoding of hex representation of p

# === Step 7: Vigenère-style decryption over printable ASCII range ===
alpha = bytes(range(32,127))       # printable ASCII range

def vig_dec(data, key):
    out, klen = bytearray(), len(key)
    for i, b in enumerate(data):
        if 32 <= b <= 126:
            pi = ((b - 32) - (key[i % klen] - 32)) % 95 + 32
            out.append(pi)
        else:
            out.append(b)
    return bytes(out)

# === Step 8: Final decryption and output ===
flag = vig_dec(rev, key).decode()
print(flag)  # GIUCTF{1SNT_R5A_N1C3?}
