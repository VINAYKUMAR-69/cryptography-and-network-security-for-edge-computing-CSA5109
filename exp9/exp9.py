p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root modulo p (g): "))
a = int(input("Alice, enter your private key (a): "))
b = int(input("Bob, enter your private key (b): "))

A = pow(g, a, p)
B = pow(g, b, p)

shared_secret_alice = pow(B, a, p)
shared_secret_bob = pow(A, b, p)

print(f"\nAlice's Public Key (A): {A}")
print(f"Bob's Public Key (B): {B}")
print(f"Alice's Computed Shared Secret: {shared_secret_alice}")
print(f"Bob's Computed Shared Secret: {shared_secret_bob}")
