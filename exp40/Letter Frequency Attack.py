from collections import Counter
import string

# Standard English letter frequency (most to least frequent)
english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def clean_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def build_mapping(cipher_freq_order, offset=0):
    return dict(zip(cipher_freq_order, english_freq_order[offset:] + english_freq_order[:offset]))

def decrypt(ciphertext, mapping):
    return ''.join(mapping.get(c, c) for c in ciphertext)

def frequency_attack(ciphertext, top_n=10):
    ciphertext = clean_text(ciphertext)
    freq = Counter(ciphertext)
    cipher_freq_order = [pair[0] for pair in freq.most_common()]

    results = []
    for offset in range(top_n):
        mapping = build_mapping(cipher_freq_order, offset)
        plaintext = decrypt(ciphertext, mapping)
        results.append((offset + 1, plaintext))
    
    return results

# Example usage
if __name__ == "__main__":
    sample_cipher = "GSRH RH Z HVXIVG NVHHZTV RH GSV XLWV"
    top_guesses = frequency_attack(sample_cipher, top_n=10)

    for rank, guess in top_guesses:
        print(f"Guess {rank}:\n{guess}\n")
