import hashlib

print("==============================")
print(" Crypto & Integrity Suite")
print("==============================")

print("1. Caesar Encrypt")
print("2. Generate SHA-256")
print("3. Generate MD5")

choice = input("Choose an option: ")

if choice == "1":
    alphabet = "abcdefghijklmnopqrstuvwxyz"

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

    print("Encrypted Text:")
    print(encrypted)

elif choice == "2":
    text = input("Enter text: ")

    result = hashlib.sha256(text.encode()).hexdigest()

    print("SHA-256:")
    print(result)

elif choice == "3":
    text = input("Enter text: ")

    result = hashlib.md5(text.encode()).hexdigest()

    print("MD5:")
    print(result)

else:
    print("Invalid choice.")
