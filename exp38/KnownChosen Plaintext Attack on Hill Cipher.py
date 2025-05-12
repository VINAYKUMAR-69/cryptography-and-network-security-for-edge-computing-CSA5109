import numpy as np
from numpy.linalg import LinAlgError

# Helper functions
def mod_inverse_matrix(matrix, modulus):
    try:
        det = int(round(np.linalg.det(matrix)))  # determinant
        det_inv = pow(det, -1, modulus)          # modular inverse of determinant
        matrix_mod_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
        )
        return matrix_mod_inv % modulus
    except (ValueError, LinAlgError):
        return None

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(int(round(num)) % 26 + ord('A')) for num in numbers)

def create_matrix_from_text(text, size):
    numbers = text_to_numbers(text)
    if len(numbers) < size * size:
        raise ValueError("Not enough characters to form square matrix")
    matrix = np.array(numbers[:size * size]).reshape(size, size)
    return matrix

def encrypt_block(plain_block, key_matrix):
    result = np.dot(key_matrix, plain_block) % 26
    return result

# Known-plaintext attack
def hill_cipher_known_plaintext_attack(plaintext, ciphertext, block_size=2):
    try:
        P = create_matrix_from_text(plaintext, block_size)
        C = create_matrix_from_text(ciphertext, block_size)

        print(f"\nPlaintext matrix (P):\n{P}")
        print(f"Ciphertext matrix (C):\n{C}")

        P_inv = mod_inverse_matrix(P, 26)
        if P_inv is None:
            print("Failed to compute inverse matrix. Try different plaintext.")
            return None

        print(f"Inverse of P mod 26:\n{P_inv}")
        K = np.dot(C, P_inv) % 26
        print(f"\nRecovered Key matrix (K):\n{K}")
        return K
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test example
if __name__ == "__main__":
    print("Known-Plaintext Attack on Hill Cipher")
    block_size = 2  # You can also test with 3 for a 3x3 key

    plaintext = input("Enter known plaintext (at least 4 letters for 2x2): ").upper()
    ciphertext = input("Enter corresponding ciphertext: ").upper()

    key = hill_cipher_known_plaintext_attack(plaintext, ciphertext, block_size)
    if key is not None:
        print("\nAttack successful. Key matrix recovered.")
