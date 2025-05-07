from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16  # AES block size is 128 bits = 16 bytes

def custom_bit_padding(data: bytes, block_size: int) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + b'\x80' + b'\x00' * (pad_len - 1)

def custom_bit_unpad(padded: bytes) -> bytes:
    if b'\x80' not in padded:
        return padded
    index = padded.rfind(b'\x80')
    return padded[:index]

def encrypt(mode: str, plaintext: bytes, key: bytes, iv: bytes = None) -> bytes:
    padded = custom_bit_padding(plaintext, BLOCK_SIZE)

    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif mode == 'CFB':
        cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    else:
        raise ValueError("Unsupported mode.")

    return cipher.encrypt(padded)

def decrypt(mode: str, ciphertext: bytes, key: bytes, iv: bytes = None) -> bytes:
    if mode == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif mode == 'CFB':
        cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    else:
        raise ValueError("Unsupported mode.")

    decrypted = cipher.decrypt(ciphertext)
    return custom_bit_unpad(decrypted)

# Sample plaintext (multiple of block size or not)
plaintext = b"This is a test message for AES modes."

# AES key and IV
key = get_random_bytes(16)
iv = get_random_bytes(16)

# ECB
print("\n--- ECB MODE ---")
ciphertext_ecb = encrypt('ECB', plaintext, key)
print("Ciphertext (hex):", ciphertext_ecb.hex())
print("Decrypted:", decrypt('ECB', ciphertext_ecb, key).decode())

# CBC
print("\n--- CBC MODE ---")
ciphertext_cbc = encrypt('CBC', plaintext, key, iv)
print("Ciphertext (hex):", ciphertext_cbc.hex())
print("Decrypted:", decrypt('CBC', ciphertext_cbc, key, iv).decode())

# CFB
print("\n--- CFB MODE ---")
ciphertext_cfb = encrypt('CFB', plaintext, key, iv)
print("Ciphertext (hex):", ciphertext_cfb.hex())
print("Decrypted:", decrypt('CFB', ciphertext_cfb, key, iv).decode())
