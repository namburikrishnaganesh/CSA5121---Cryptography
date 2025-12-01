import string
alphabet = string.ascii_uppercase
def caesar(s, k):
    r = []
    for c in s:
        if c in alphabet:
            r.append(alphabet[(alphabet.index(c) + k) % 26])
        else:
            r.append(c)
    return "".join(r)
text = input()
k = int(input())
print(caesar(text, k))
