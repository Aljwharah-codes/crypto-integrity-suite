alphabet = "abcdefghijklmnopqrstuvwxyz"

print("=== Caesar Cipher Encryption ===")

text = input("Enter text: ").lower()
shift = int(input("Enter shift value: "))

encrypted = ""

for letter in text:
    if letter in alphabet:
        index = alphabet.index(letter)
        new_index = (index + shift) % 26
        encrypted += alphabet[new_index]
    else:
        encrypted += letter

print("\nEncrypted Text:")
print(encrypted)
