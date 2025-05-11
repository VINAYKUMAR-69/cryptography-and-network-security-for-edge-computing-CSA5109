from math import gcd

# Affine Cipher Encryption: C = (a * p + b) mod 26
def encrypt_affine(p, a, b):
    return (a * p + b) % 26

# Decryption: p = a_inv * (C - b) mod 26
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  # No modular inverse if gcd(a, m) != 1

def decrypt_affine(c, a, b):
    a_inv = modinv(a, 26)
    if a_inv is None:
        raise ValueError("a has no modular inverse modulo 26")
    return (a_inv * (c - b)) % 26

# Check if cipher is one-to-one by ensuring gcd(a, 26) == 1
def is_one_to_one(a):
    return gcd(a, 26) == 1

# Example usage
a, b = 5, 8  # Try changing to (2, 3) for a non one-to-one cipher
if is_one_to_one(a):
    plaintext = "HELLO"
    encrypted = [encrypt_affine(ord(c) - 65, a, b) for c in plaintext]
    ciphertext = ''.join(chr(c + 65) for c in encrypted)
    
    decrypted_nums = [decrypt_affine(c, a, b) for c in encrypted]
    decrypted_text = ''.join(chr(p + 65) for p in decrypted_nums)
    
    print("Plaintext: ", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted: ", decrypted_text)
else:
    print(f"The key a = {a} is invalid (gcd({a}, 26) ≠ 1), cipher not one-to-one.")
