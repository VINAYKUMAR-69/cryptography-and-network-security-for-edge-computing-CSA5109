def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

msg = input("Enter message: ")
s = int(input("Enter shift: "))

encrypted = caesar_cipher(msg, s)
print("Encrypted:", encrypted)

decrypted = caesar_cipher(encrypted, -s)
print("Decrypted:", decrypted)
