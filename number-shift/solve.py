# Number Shift Solver for GIU-CTF 2025
hex_values = "64 6d 71 72 74 78 77 69 69 75 66".split()
cipher_bytes = [int(h, 16) for h in hex_values]

key = [3, 1, 4]  # Repeating numeric key
decoded_chars = []

for i, byte in enumerate(cipher_bytes):
    shift = key[i % len(key)]
    decoded_chars.append(chr(byte - shift))

flag = ''.join(decoded_chars)
print("Flag: GIUCTF{" + flag + "}")