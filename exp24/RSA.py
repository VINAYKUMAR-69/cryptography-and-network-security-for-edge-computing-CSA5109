def extended_euclid(a, b):
    """Returns (gcd, x, y) such that a*x + b*y = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi_n):
    """Returns the modular inverse of e modulo phi_n using the extended Euclidean algorithm."""
    gcd, x, _ = extended_euclid(e, phi_n)
    if gcd != 1:
        raise ValueError(f"e = {e} and phi(n) = {phi_n} are not coprime, so no modular inverse exists.")
    return x % phi_n

def find_primes(n):
    """Finds primes p and q such that p * q = n using trial and error."""
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            q = n // p
            return p, q
    return None, None

# Given public key
e = 31
n = 3599

# Step 1: Find p and q such that n = p * q
p, q = find_primes(n)
print(f"Found p = {p} and q = {q}")

# Step 2: Compute Euler's Totient function, phi(n) = (p - 1) * (q - 1)
phi_n = (p - 1) * (q - 1)
print(f"phi(n) = {phi_n}")

# Step 3: Find the private key d by computing the modular inverse of e modulo phi(n)
d = mod_inverse(e, phi_n)
print(f"Private key (d) = {d}")
