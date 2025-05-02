import math

def format_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def create_matrix(plaintext, cols):
    rows = math.ceil(len(plaintext) / cols)
    matrix = [['X' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for i in range(rows):
        for j in range(cols):
            if index < len(plaintext):
                matrix[i][j] = plaintext[index]
                index += 1
    return matrix

def get_sorted_key_order(keyword):
    return sorted(list(enumerate(keyword)), key=lambda x: x[1])

def encrypt_columnar(plaintext, keyword):
    plaintext = format_text(plaintext)
    cols = len(keyword)
    matrix = create_matrix(plaintext, cols)
    key_order = get_sorted_key_order(keyword)
    
    ciphertext = ''
    for idx, _ in key_order:
        for row in matrix:
            ciphertext += row[idx]
    return ciphertext


plaintext = "WE ARE DISCOVERED RUN"
keyword = "ZEBRAS"


ciphertext = encrypt_columnar(plaintext, keyword)
print("Plaintext:", plaintext)
print("Keyword:  ", keyword)
print("Ciphertext:", ciphertext)
