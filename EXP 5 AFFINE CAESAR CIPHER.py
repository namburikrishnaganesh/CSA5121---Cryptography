import math
def mod_inverse(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None
a = int(input("enter value for 'a' (must be coprime to 26): "))
b = int(input("enter value for 'b': "))
pt = input("enter the pt : ")
pt2 = "".join(c for c in pt.upper() if c.isalpha())
ct = ""
for ch in pt2:
    p = ord(ch) - 65
    c = (a * p + b) % 26
    ct += chr(c + 65)
a_inv = mod_inverse(a, 26)
dt = ""
for ch in ct:
    c = ord(ch) - 65
    p = (a_inv * (c - b)) % 26
    dt += chr(p + 65)
print("decrypted:", dt)
