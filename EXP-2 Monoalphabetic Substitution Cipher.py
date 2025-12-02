import string
alphabet = string.ascii_uppercase
key = input("Enter substitution key (26 letters): ").upper()
mapping = {alphabet[i]: key[i] for i in range(26)}
plaintext = input("Enter plain text: ").upper()
ciphertext = ""
for ch in plaintext:
    if ch in mapping:
        ciphertext += mapping[ch]
    else:
        ciphertext += ch
print("CIPHER TEXT :", ciphertext)
