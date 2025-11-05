# SCT_CS_01
A simple Python implementation of the classic Caesar Cipher encryption and decryption technique. This command-line tool allows users to encode or decode messages by shifting letters in the alphabet by a specified number of positions. 

 Caesar Cipher Program
A simple Python implementation of the classic Caesar Cipher encryption and decryption technique. This command-line tool allows users to encode or decode messages by shifting letters in the alphabet by a specified number of positions.

 Description
The Caesar Cipher is one of the oldest known encryption techniques. It works by shifting each letter in a message by a fixed number of positions down the alphabet. This project provides:

- A function to encrypt messages using a Caesar shift
- A function to decrypt messages using the reverse shift
- A command-line interface for user interaction

This tool is ideal for learning basic cryptography concepts and practicing Python programming.

 Features
- Encrypts and decrypts alphabetic messages
- Preserves case (uppercase/lowercase)
- Ignores non-alphabetic characters (punctuation, numbers, spaces)
- Simple and interactive command-line interface

 How It Works
- For encryption: each letter is shifted forward by the given number.
- For decryption: each letter is shifted backward by the same number.
- Non-letter characters remain unchanged.

Usage

1. Clone the repository:
   bash
   git clone https://github.com/your-username/caesar-cipher.git
   cd caesar-cipher

2. Run the program:
   bash
   python caesar_cipher.py


3. Follow the prompts:
   - Choose to encrypt or decrypt
   - Enter your message
   - Enter the shift value (integer)


 Example
Caesar Cipher Program
Type 'encrypt' to encrypt or 'decrypt' to decrypt: encrypt
Enter your message: Hello, World!
Enter shift value (integer): 3
Encrypted message: Khoor, Zruog!
