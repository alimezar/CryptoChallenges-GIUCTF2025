# The Fragmented Key (150 pts) — Medium

## 🧠 Main Idea

While sweeping a compromised file system, forensic analysts unearthed a fragmented message and a cryptic note. What they found wasn't encrypted in the usual way. The message had been twisted not through letters alone, but across the full range of bytes — obscured by a shifting key born from strange fragments.

This is no ordinary Caesar cipher. This is something deeper — **a byte-wise cipher**, where each character in the message was shifted using a **repeating key derived from hidden strings**.

---

## 🧩 Challenge Premise

You're provided with:

- An encrypted message (`message.txt`)
- A list of potential key fragments (`fragments.txt`)
- A mysterious note left behind (`note.txt`)

The note says:

> “The message was encrypted with a repeating Vigenère key derived from three of the five fragments, in order.  
> For each chosen fragment, add the ASCII values of its characters, convert the sum to base-36, then concatenate the three base-36 strings to build the final Vigenère key.”

---

## 🕵️ What You Need to Do

1. **Understand the encryption logic.**  
   The cipher is not working over letters — it's treating characters as bytes (0–255). The key used is repeating, and not directly readable — it must be **derived**.

2. **Interpret the clue.**  
   - Choose **3 out of the 5 fragments**, and preserve their **order**.
   - For each:
     - Add the ASCII values of its characters.
     - Convert the result to **base-36** (digits + lowercase letters).
   - Concatenate the 3 base-36 numbers → this becomes your key (as bytes).

3. **Decrypt the message.**  
   - The message is base64-encoded. First, decode it.
   - Then apply **byte-wise Vigenère decryption** using your derived key.
   - Repeat the key as needed to match the length of the message.
   - If you find readable text starting with `GIUCTF{...}`, you've succeeded.

---

## 📂 Files Included

- `message.txt` — The encrypted message (base64)
- `fragments.txt` — Potential key fragment strings
- `note.txt` — A critical hint on how the encryption was applied

---

## 🧪 What You’ll Learn

This challenge teaches:
- How to derive encryption keys through obfuscated transformation logic
- Working with non-standard alphabets and byte-wise encryption
- Applying modular arithmetic and pattern recognition in cryptanalysis

The difficulty lies in connecting layers: **fragments → numbers → base36 → bytes → decryption**. Mastering that sequence unlocks the flag.

---

## 🏁 Flag Format

Submit the flag in this format once you find it:

GIUCTF{your_answer_here}