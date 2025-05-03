def text_to_bits(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def bits_to_text(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def xor_bits(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def encrypt_block(block):
    left = block[:32]
    right = block[32:]
    new_left = right
    new_right = xor_bits(left, right)
    return new_left + new_right

def encrypt(plaintext):
    bits = text_to_bits(plaintext)
    
    # Pad the bits to be a multiple of 64
    while len(bits) % 64 != 0:
        bits += '0'

    ciphertext = ''
    for i in range(0, len(bits), 64):
        block = bits[i:i+64]
        encrypted_block = encrypt_block(block)
        ciphertext += encrypted_block

    return ciphertext

def decrypt_block(block):
    left = block[:32]
    right = block[32:]
    orig_right = left
    orig_left = xor_bits(left, right)
    return orig_left + orig_right

def decrypt(ciphertext_bits):
    plaintext_bits = ''
    for i in range(0, len(ciphertext_bits), 64):
        block = ciphertext_bits[i:i+64]
        decrypted_block = decrypt_block(block)
        plaintext_bits += decrypted_block

    return bits_to_text(plaintext_bits).rstrip('\x00')

# 🔽 User Input Section
if __name__ == "__main__":
    user_input = input("Enter plaintext to encrypt: ")
    encrypted = encrypt(user_input)
    print("Encrypted binary:", encrypted)

    decrypted = decrypt(encrypted)
    print("Decrypted text:", decrypted)
