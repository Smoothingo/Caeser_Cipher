import os

def caesar_cipher(text, key, mode):
    """Applies a Caesar cipher to the input text using the given key and mode."""
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the key value
            shifted = ord(char) + key * mode
            # Handle wraparound for letters outside the alphabet
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            else:
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt_without_key(ciphertext):
    """Decrypts the ciphertext without knowing the key by brute-force."""
    with open("decryptbrute.txt", "w") as output_file:
        for key in range(26):
            plaintext = caesar_cipher(ciphertext, key, -1)
            output_file.write(f"Key: {key}\n")
            output_file.write(plaintext + "\n\n")
    print("Output written to decryptbrute.txt")

# Read input file
input_file_path = os.path.abspath('text.txt')
with open(input_file_path, 'r') as input_file:
    plaintext = input_file.read()

# Get user input for encryption/decryption and key value
while True:
    mode = input("Enter '1' to encrypt, '2' to decrypt with key, '3' to decrypt without key, or '4' to exit: ")
    if mode in ['1', '2', '3', '4']:
        mode = int(mode)
        if mode == 4:
            break
        elif mode == 1:
            key = input("Enter a key value: ")
            if key.isdigit():
                key = int(key)
                output_file_name = "encrypt.txt"
                with open(output_file_name, 'w') as output_file:
                    ciphertext = caesar_cipher(plaintext, key, 1)
                    output_file.write(ciphertext)
                    print(f"Ciphertext written to {output_file_name}")
            else:
                print("Invalid key value entered")
        elif mode == 2:
            key = input("Enter the key value: ")
            if key.isdigit():
                key = int(key)
                input_file_path = input("Enter the input file name: ")
                with open(input_file_path, 'r') as input_file:
                    ciphertext = input_file.read()
                    plaintext = caesar_cipher(ciphertext, key, -1)
                    output_file_name = "decryptkey.txt"
                    with open(output_file_name, 'w') as output_file:
                        output_file.write(plaintext)
                    print(f"Output written to {output_file_name}")
            else:
                print("Invalid key value entered")
        elif mode == 3:
            input_file_path = "text.txt"
            with open(input_file_path, 'r') as input_file:
                ciphertext = input_file.read()
                decrypt_without_key(ciphertext)
        else:
            print("Invalid mode entered")
    else:
        print("Invalid mode entered")
