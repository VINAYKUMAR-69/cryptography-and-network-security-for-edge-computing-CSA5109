def rsa_encrypt(m, e, n):
    return pow(m, e, n)

e = 17
n = 3233

cipher_dict = {rsa_encrypt(i, e, n): chr(i + 65) for i in range(26)}

message = "HELLO"
plaintext_numbers = [ord(c) - 65 for c in message]
ciphertext = [rsa_encrypt(p, e, n) for p in plaintext_numbers]

print("Ciphertext:", ciphertext)
recovered = ''.join(cipher_dict[c] for c in ciphertext)
print("Recovered message:", recovered)
