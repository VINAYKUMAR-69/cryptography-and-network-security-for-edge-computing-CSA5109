def permute(bits, pattern):
    return ''.join(bits[i] for i in pattern)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def sbox_lookup(sbox, bits):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')

def generate_subkeys(key10):
    p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    p8 = [5, 2, 6, 3, 7, 4, 9, 8]
    key_permuted = permute(key10, p10)
    left, right = key_permuted[:5], key_permuted[5:]
    left1 = left_shift(left, 1)
    right1 = left_shift(right, 1)
    k1 = permute(left1 + right1, p8)
    left2 = left_shift(left1, 2)
    right2 = left_shift(right1, 2)
    k2 = permute(left2 + right2, p8)
    return k1, k2

def fk(bits, subkey):
    ep = [3, 0, 1, 2, 1, 2, 3, 0]
    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]
    left, right = bits[:4], bits[4:]
    right_expanded = permute(right, ep)
    xor_result = xor(right_expanded, subkey)
    s0_result = sbox_lookup(s0, xor_result[:4])
    s1_result = sbox_lookup(s1, xor_result[4:])
    p4 = permute(s0_result + s1_result, [1, 3, 2, 0])
    return xor(left, p4) + right

def sdes_encrypt(plain8, k1, k2):
    ip = [1, 5, 2, 0, 3, 7, 4, 6]
    ip_inv = [3, 0, 2, 4, 6, 1, 7, 5]
    bits = permute(plain8, ip)
    bits = fk(bits, k1)
    bits = bits[4:] + bits[:4]
    bits = fk(bits, k2)
    return permute(bits, ip_inv)

def sdes_decrypt(cipher8, k1, k2):
    return sdes_encrypt(cipher8, k2, k1)  # Just reverse the keys

def ctr_encrypt(plaintext_bits, key10, counter_start):
    k1, k2 = generate_subkeys(key10)
    blocks = [plaintext_bits[i:i+8] for i in range(0, len(plaintext_bits), 8)]
    counter = int(counter_start, 2)
    ciphertext = ""
    for block in blocks:
        ctr_bin = format(counter, '08b')
        keystream = sdes_encrypt(ctr_bin, k1, k2)
        ciphertext_block = xor(block, keystream)
        ciphertext += ciphertext_block
        counter += 1
    return ciphertext

def ctr_decrypt(ciphertext_bits, key10, counter_start):
    return ctr_encrypt(ciphertext_bits, key10, counter_start)  # Same as encryption

# Inputs
plaintext = '000000010000001000000100'
key = '0111111101'
counter = '00000000'

# Encrypt
ciphertext = ctr_encrypt(plaintext, key, counter)
print("Ciphertext :", ciphertext)

# Decrypt
decrypted = ctr_decrypt(ciphertext, key, counter)
print("Decrypted  :", decrypted)
