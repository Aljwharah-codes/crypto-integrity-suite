import hashlib

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


def generate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()


print("=" * 40)
print(" Crypto & Integrity Cipher Suite ")
print("=" * 40)

while True:

    print("\nChoose an option:")
    print("1. Caesar Encrypt")
    print("2. Caesar Decrypt")
    print("3. Generate SHA-256")
    print("4. Generate MD5")
    print("5. Compare Hashes")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))

        print("\nEncrypted Text:")
        print(caesar_encrypt(text, shift))

    elif choice == "2":
        text = input("Enter encrypted text: ")
        shift = int(input("Enter shift value: "))

        print("\nDecrypted Text:")
        print(caesar_decrypt(text, shift))

    elif choice == "3":
        text = input("Enter text: ")

        print("\nSHA-256 Hash:")
        print(generate_sha256(text))

    elif choice == "4":
        text = input("Enter text: ")

        print("\nMD5 Hash:")
        print(generate_md5(text))

    elif choice == "5":
        hash1 = input("Enter first hash: ")
        hash2 = input("Enter second hash: ")

        if hash1 == hash2:
            print("\n✅ Integrity Verified")
            print("The hashes match.")
        else:
            print("\n⚠️ Warning!")
            print("The hashes do NOT match.")
            print("The data may have been modified.")

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
