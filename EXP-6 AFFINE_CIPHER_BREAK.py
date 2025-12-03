from collections import Counter
import math
def to_num(ch):
    return ord(ch) - ord('A')
def to_char(n):
    return chr(n + ord('A'))
def mod_inverse(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None
def solve_key(c1, c2):
    E = to_num('E')
    T = to_num('T')
    diff_c = (c1 - c2) % 26
    diff_p = (E - T) % 26
    inv = mod_inverse(diff_p, 26)
    if inv is None:
        return None, None
    a = (diff_c * inv) % 26
    b = (c1 - a * E) % 26
    return a, b
def decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    plaintext = ""
    for ch in cipher:
        if ch.isalpha():
            c = to_num(ch)
            p = (a_inv * (c - b)) % 26
            plaintext += to_char(p)
        else:
            plaintext += ch
    return plaintext
ciphertext = input("Enter ciphertext: ").upper()
freq = Counter([c for c in ciphertext if c.isalpha()])
most_common = [x[0] for x in freq.most_common(2)]
C1 = to_num(most_common[0])
C2 = to_num(most_common[1])  
a, b = solve_key(C1, C2)
if a is None:
    print("Key could not be solved (no modular inverse).")
else:
    print(f"Recovered key: a = {a}, b = {b}")
    plaintext = decrypt(ciphertext, a, b)
    print("Decrypted text =", plaintext)
