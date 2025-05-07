from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    while True:
        try:
            key = get_random_bytes(24)
            return DES3.adjust_key_parity(key)
        except ValueError:
            continue

def encrypt_3des_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_data = pad(plaintext, DES3.block_size)
    return cipher.encrypt(padded_data)

def decrypt_3des_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, DES3.block_size)

if __name__ == "__main__":
    plaintext = b"This is a top secret message!"
    key = generate_key()
    iv = get_random_bytes(8)

    ciphertext = encrypt_3des_cbc(plaintext, key, iv)
    print("Ciphertext (hex):", ciphertext.hex())

    decrypted = decrypt_3des_cbc(ciphertext, key, iv)
    print("Decrypted text:", decrypted.decode())
