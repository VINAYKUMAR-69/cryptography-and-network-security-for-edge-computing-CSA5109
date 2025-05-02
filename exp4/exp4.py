def construct_vigenere_table():
    table = []
    for i in range(26):
        row = [chr((i + j) % 26 + ord('A')) for j in range(26)]
        table.append(row)
    return table

def format_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def generate_full_key(plaintext, keyword):
    keyword = keyword.upper()
    repeated_key = ''
    for i in range(len(plaintext)):
        repeated_key += keyword[i % len(keyword)]
    return repeated_key

def encrypt_vigenere(plaintext, keyword):
    table = construct_vigenere_table()
    plaintext = format_text(plaintext)
    keyword = generate_full_key(plaintext, keyword)
    ciphertext = ''
    for p_char, k_char in zip(plaintext, keyword):
        row = ord(k_char) - ord('A')
        col = ord(p_char) - ord('A')
        cipher_char = table[row][col]
        ciphertext += cipher_char
    return ciphertext

# Input from user
plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

ciphertext = encrypt_vigenere(plaintext, keyword)
print("Cipher Text:", ciphertext)
