from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'secret.key'")

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("No key found. Generating a new key...")
        generate_key()
        return open("secret.key", "rb").read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    
    print(f"File '{file_path}' encrypted successfully.")

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    
    print(f"File '{file_path}' decrypted successfully.")

def main():
    while True:
        choice = input("Do you want to (G)enerate a new key, (E)ncrypt, (D)ecrypt a file, or (Q)uit? ").upper()
        if choice == 'G':
            generate_key()
        elif choice == 'E':
            file_path = input("Enter the path of the file to encrypt: ")
            if os.path.isfile(file_path):
                encrypt_file(file_path)
            else:
                print("File not found.")
        elif choice == 'D':
            file_path = input("Enter the path of the file to decrypt: ")
            if os.path.isfile(file_path):
                decrypt_file(file_path)
            else:
                print("File not found.")
        elif choice == 'Q':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
