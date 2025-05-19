# Sum of Secrets (500 pts) — Very Hard

## 🧠 Main Idea

RSA is one of the most trusted encryption schemes in modern cryptography — when implemented correctly. But what happens when the cryptosystem leaks just a little too much?

This challenge gives you a **public RSA key**, a **ciphertext**, and one suspicious extra value: `S`. There are no hints. But if you notice the structure — and know your number theory — a complete break becomes possible.

---

## 🧩 Challenge Premise

You are given:

- `public.txt` — contains:
  - `N` (modulus)
  - `e` (public exponent)
  - `S` (the sum of the two primes, `p + q`)
- `ciphertext.bin` — an RSA-encrypted file (ciphertext)

Your mission is to:
1. **Factor `N`**, but not through brute force.
2. **Recover `p` and `q`** using the fact that:
   - `S = p + q`
   - `N = p * q`
   - Use these two equations to solve a quadratic.
3. **Decrypt the ciphertext** using standard RSA private key derivation.
4. **Reverse the plaintext** (it was stored backwards).
5. **Apply a Vigenère-style decryption**, using the ASCII form of `p` as the key.

---

## 🛠️ What You Need to Figure Out

- Use `S² - 4N` to get the discriminant of the quadratic:
  - `(p + q)² - 4pq = (p - q)²`
  - This is a perfect square — so `sqrtD = √(S² - 4N)`
- Compute `p = (S + sqrtD)/2`, `q = (S - sqrtD)/2`
- With `p`, `q`, and `e`, compute the RSA private exponent `d`
- Decrypt the ciphertext: `m = c^d mod N`
- Convert the plaintext to bytes and reverse it
- Use a Vigenère cipher (ASCII range 32–126) to decrypt the reversed bytes using the ASCII of `hex(p)[2:]` as the key

---

## 🧪 Educational Outcome

This challenge simulates a real-world RSA failure where a system leaks an auxiliary parameter — the **sum of the primes**. While seemingly harmless, this opens the door to direct factoring by solving a quadratic.

It also teaches:
- RSA internals: factoring, modular inverse, private exponent
- How small metadata leaks (like `p + q`) can completely destroy security
- Byte-level Vigenère as a final twist for obfuscation

---

## 🧩 Flag Format

GIUCTF{your_answer_here}

---

## 📂 Files Included

- `public.txt` — Contains the RSA public key and leaked sum
- `ciphertext.bin` — Encrypted binary message
