def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    if choice == 'encrypt':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'decrypt':
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
