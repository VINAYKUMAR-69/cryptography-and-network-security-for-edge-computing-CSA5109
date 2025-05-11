from Crypto.PublicKey import DSA, RSA
from Crypto.Signature import DSS, pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

message = b"This is a secure message"

# --- DSA Signatures ---
dsa_key = DSA.generate(2048)
hasher = SHA256.new(message)
signer_dsa = DSS.new(dsa_key, 'fips-186-3')

signature1_dsa = signer_dsa.sign(hasher)
signature2_dsa = signer_dsa.sign(SHA256.new(message))  # sign again

# --- RSA Signatures ---
rsa_key = RSA.generate(2048)
signer_rsa = pkcs1_15.new(rsa_key)

signature1_rsa = signer_rsa.sign(SHA256.new(message))
signature2_rsa = signer_rsa.sign(SHA256.new(message))  # sign again

print("DSA Signature 1 == Signature 2:", signature1_dsa == signature2_dsa)
print("RSA Signature 1 == Signature 2:", signature1_rsa == signature2_rsa)
