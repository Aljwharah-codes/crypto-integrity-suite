import hashlib

# -----------------------------
# Caesar Cipher Functions
# -----------------------------

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


# -----------------------------
# Vigenère Cipher
# -----------------------------

def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


# -----------------------------
# Hash Functions
# -----------------------------

def generate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()


def compare_hashes(hash1, hash2):
    return hash1 == hash2


# -----------------------------
# Main Program
# -----------------------------

while True:

    print("\n===================================")
    print(" Crypto & Integrity Cipher Suite ")
    print("===================================")

    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. Vigenère Encrypt")
    print("4. Generate SHA-256")
    print("5. Generate MD5")
    print("6. Compare Hashes")
    print("7. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Shift: "))

        print("\nEncrypted Text:")
        print(caesar_encrypt(text, shift))

    elif choice == "2":
        text = input("Enter encrypted text: ")
        shift = int(input("Shift: "))

        print("\nDecrypted Text:")
        print(caesar_decrypt(text, shift))

    elif choice == "3":
        text = input("Enter text: ")
        key = input("Enter key: ")

        print("\nEncrypted Text:")
        print(vigenere_encrypt(text, key))

    elif choice == "4":
        text = input("Enter text: ")

        print("\nSHA-256:")
        print(generate_sha256(text))

    elif choice == "5":
        text = input("Enter text: ")

        print("\nMD5:")
        print(generate_md5(text))

    elif choice == "6":
        hash1 = input("Enter first hash: ")
        hash2 = input("Enter second hash: ")

        if compare_hashes(hash1, hash2):
            print("\n✅ Integrity Verified")
            print("Both hashes match.")
        else:
            print("\n⚠️ Warning!")
            print("Hashes do not match.")
            print("Data may have been modified.")

    elif choice == "7":
        print("\nThank you for using Crypto & Integrity Cipher Suite.")
        break

    else:
        print("\nInvalid option. Please try again.")
