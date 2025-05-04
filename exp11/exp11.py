import hashlib
import random

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(k, q):
    gcd, x, _ = gcd_extended(k, q)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    return x % q

def sha1_hash(message):
    return int(hashlib.sha1(message.encode()).hexdigest(), 16)

p = 467
q = 233
g = 2

x = random.randint(1, q - 1)
y = pow(g, x, p)

message = input("Enter message: ")
h = sha1_hash(message) % q

k = random.randint(1, q - 1)
r = pow(g, k, p) % q
k_inv = mod_inverse(k, q)
s = (k_inv * (h + x * r)) % q

print("\nDigital Signature:")
print("r =", r)
print("s =", s)

w = mod_inverse(s, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print("\nVerification:")
print("v =", v)
print("Signature is valid." if v == r else "Signature is invalid.")
