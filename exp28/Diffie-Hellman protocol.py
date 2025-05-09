q = 353
a = 3

alice_secret = 97
bob_secret = 233

alice_public = pow(a, alice_secret, q)
bob_public = pow(a, bob_secret, q)

alice_key = pow(bob_public, alice_secret, q)
bob_key = pow(alice_public, bob_secret, q)

print("Shared key (Alice):", alice_key)
print("Shared key (Bob):", bob_key)
