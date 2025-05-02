import numpy as np

def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr(int(n) + ord('A'))

def get_key_matrix(key):
    return np.array([char_to_num(c) for c in key]).reshape(3, 3)

def process_text(text):
    text = text.upper().replace(" ", "")
    while len(text) % 3 != 0:
        text += 'X'
    return text

def encrypt(plaintext, key_matrix):
    plaintext = process_text(plaintext)
    numbers = [char_to_num(c) for c in plaintext]
    chunks = [numbers[i:i+3] for i in range(0, len(numbers), 3)]
    ciphertext = ''
    for chunk in chunks:
        vector = np.array(chunk).reshape(3, 1)
        result = np.dot(key_matrix, vector) % 26
        ciphertext += ''.join(num_to_char(n) for n in result.flatten())
    return ciphertext

key_input = input("Enter a 9-letter key: ")
plaintext_input = input("Enter plaintext: ")

key_matrix = get_key_matrix(key_input)
cipher_text = encrypt(plaintext_input, key_matrix)

print("Cipher Text:", cipher_text)
