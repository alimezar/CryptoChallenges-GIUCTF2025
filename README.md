# 🔐 CryptoChallenges-GIUCTF2025

Welcome to the official cryptography category for **GIU-CTF 2025**, crafted and hosted by [Ali Sherif](https://www.linkedin.com/in/ali-sherif-13812b276/).

This repository contains all the original cryptography challenges that appeared in the competition — ranging from beginner puzzles to real-world inspired RSA breaks. Each challenge includes its full context, story, input files, and a structured write-up or README.

> “Crypto done wrong tells you a story.  
> Crypto done right tells you nothing.  
> These challenges tell you... just enough.”

---

## 🗂️ Challenge Index

| Challenge Name        | Difficulty | Points | Description                                               |
|------------------------|------------|--------|-----------------------------------------------------------|
| [Number Shift](challenges/Number-Shift)          | Easy       | 75     | Caesar-style cipher with a repeating numeric twist         |
| [The Fragmented Key](challenges/The-Fragmented-Key)  | Medium     | 150    | Vigenère decryption with base36 fragment-based key logic   |
| [Military-Grade-Enc](https://github.com/alimezar/military-grade-enc) | Hard       | 300    | Web crypto disaster with DES, padding leaks, and backups   |
| [Sum of Secrets](challenges/Sum-Of-Secrets)      | Very Hard  | 500    | RSA with leaked p + q — recover the key and decrypt the flag |

---

## 📦 Folder Structure

```plaintext
challenges/
├── number-shift/         ← Hex + Caesar cipher challenge
├── fragmented-key/       ← Fragment-based Vigenère key challenge
├── military-grade-enc/   ← External link to Dockerized web crypto challenge
├── sum-of-secrets/       ← RSA with twist & layered decryption

```
---

Each folder contains:
- `README.md` — challenge story and solving instructions
- `challenge.md` — metadata for CTFd-style platforms
- Input files (`.txt`, `.bin`, etc.)
- `flag.txt` — official flag for validation (private)
- `solve.py` — staff-only solution script (excluded from in-game view)

---

## 🧪 Educational Themes

These challenges explore topics like:

- Caesar & Vigenère variations  
- Base conversions and ASCII manipulation  
- Brute-force resilience through logic-based encryption  
- Cryptographic flaws (DES, padding, RSA leakage)  
- Byte-level ciphers and key schedule mismanagement

---

## 🏁 Flag Format

All flags follow the format:
GIUCTF{...}


---

## 📜 License

This challenge set is released under the MIT License for educational and ethical hacking use. Attribution is appreciated.

---

## 🧠 Author

Made with 💻, 🔐, and ☕ by **Ali Sherif**  
GitHub: [@alimezar](https://github.com/alimezar)  
LinkedIn: [Ali Sherif](https://www.linkedin.com/in/ali-sherif-13812b276/)
