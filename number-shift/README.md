# Number Shift (75 pts) — Easy

## 🧠 Main Idea

This challenge introduces players to a simple variant of the Caesar Cipher. Instead of a fixed key, a short **repeating numeric key** is used to shift each byte **backward** to recover the original message.

It starts with hexadecimal numbers, which convert to shifted ASCII characters. The player must:

1. Convert hex to decimal.
2. Reverse the shift using the repeating numeric key (e.g., 3, 1, 4).
3. Reconstruct the original string to reveal the flag.

This challenge builds intuition for:
- Hexadecimal to ASCII conversion
- Caesar Cipher with variable (repeating) keys

---

## 🧩 How to Solve

1. Open `NumberShift.txt` and copy the hex values:
64 6d 71 72 74 78 77 69 69 75 66

2. Convert these hex values to decimal:
[100, 109, 113, 114, 116, 120, 119, 105, 105, 117, 102]


3. Notice that the difference between characters varies. Use the **hint** to try a **repeating 3-digit numeric key** from 1–9, such as `3 1 4`.

4. Subtract those values in order from the decimal list:
- 100 - 3 → 'a'
- 109 - 1 → 'l'
- 113 - 4 → 'm'
- ...

5. You’ll reveal the plaintext:
almostthere

6. Wrap it in the required format:
GIUCTF{almostthere}


---

## 🧪 Educational Outcome

This challenge teaches basic transformation layering — where multiple light steps obscure the real message:
- Layer 1: Hex encoding
- Layer 2: Repeating Caesar key

It rewards pattern recognition and basic decryption skills.

---

## 📂 Files

- `NumberShift.txt` — The input hex values
- `solve.py` — Script that decodes and solves the challenge
- `flag.txt` — The flag for verification
- `challenge.md` — CTFd-style metadata for the challenge
