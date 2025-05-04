import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, z):
    t, new_t = 0, 1
    r, new_r = z, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise Exception("e is not invertible")
    if t < 0:
        t += z
    return t

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

p = 61
q = 53
n = p * q
z = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, z)

print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")

message = 42
cipher = mod_exp(message, e, n)
print(f"Original Message: {message}")
print(f"Encrypted Message: {cipher}")

decrypted = mod_exp(cipher, d, n)
print(f"Decrypted Message: {decrypted}")
