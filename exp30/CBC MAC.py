from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def xor_bytes(b1, b2):
    return bytes(x ^ y for x, y in zip(b1, b2))

def cbc_mac(key, message):
    cipher = AES.new(key, AES.MODE_CBC, iv=bytes(16))
    padded = pad(message, AES.block_size)
    return cipher.encrypt(padded)[-AES.block_size:]

key = get_random_bytes(16)
X = b'SingleBlockMsg!'  # 15 bytes
T = cbc_mac(key, X)

X_xor_T = xor_bytes(X, T)
forged_message = X + X_xor_T
forged_mac = cbc_mac(key, forged_message)

print("Original MAC T:    ", T.hex())
print("Forged MAC (T2):   ", forged_mac.hex())
print("MAC forgery valid: ", T == forged_mac)
