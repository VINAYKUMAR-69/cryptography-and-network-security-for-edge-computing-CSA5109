from collections import Counter
import string

# English letter frequency from most to least common
english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def letter_frequency_attack(ciphertext, top_n=5):
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    freq = Counter(ciphertext)
    sorted_cipher_letters = [item[0] for item in freq.most_common()]
    
    # Generate possible mappings using frequency rankings
    guesses = []
    for i in range(top_n):
        mapping = {}
        for j, c in enumerate(sorted_cipher_letters):
            if j < len(english_freq_order):
                mapping[c] = english_freq_order[(j + i) % len(english_freq_order)]
        
        # Substitute based on the mapping
        decrypted = ''.join(mapping.get(ch, ch) for ch in ciphertext)
        guesses.append(decrypted)
    
    return guesses

# Example usage
ciphertext = "ZPV IBWF CFFO DPNQSPNJTFE! UIFTF DPEFT BSF OPU FBTZ UP DSBDL."
top_plaintexts = letter_frequency_attack(ciphertext, top_n=5)

for i, text in enumerate(top_plaintexts, 1):
    print(f"Guess {i}: {text}")
