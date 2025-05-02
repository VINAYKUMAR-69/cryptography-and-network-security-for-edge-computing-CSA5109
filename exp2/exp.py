def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result

def playfair_encrypt(text, matrix):
    text = prepare_text(text)
    encrypted = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            encrypted += matrix[r1][(c1 + 1) % 5]
            encrypted += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            encrypted += matrix[(r1 + 1) % 5][c1]
            encrypted += matrix[(r2 + 1) % 5][c2]
        else:
            encrypted += matrix[r1][c2]
            encrypted += matrix[r2][c1]
    return encrypted

def playfair_decrypt(text, matrix):
    decrypted = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            decrypted += matrix[r1][(c1 - 1) % 5]
            decrypted += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            decrypted += matrix[(r1 - 1) % 5][c1]
            decrypted += matrix[(r2 - 1) % 5][c2]
        else:
            decrypted += matrix[r1][c2]
            decrypted += matrix[r2][c1]
    return decrypted

# === Main Program ===
key = input("Key: ")
message = input("Message: ")

matrix = generate_matrix(key)

encrypted = playfair_encrypt(message, matrix)
decrypted = playfair_decrypt(encrypted, matrix)

print("\nPlayfair Matrix:")
for row in matrix:
    print(' '.join(row))

print("\nEncrypted:", encrypted)
print("Decrypted:", decrypted)
