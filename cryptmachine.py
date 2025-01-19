def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter your text: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        print("Encrypted text: ", encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted text: ", decrypt(text, shift))
    else:
        print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")
