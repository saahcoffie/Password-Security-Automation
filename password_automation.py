import random
import string
import re

def is_strong_password(password):
    if (len(password) < 8 or
        not any(char.isupper() for char in password) or
        not any(char.islower() for char in password) or
        not any(char.isdigit() for char in password) or
        not any(char in string.punctuation for char in password)):
        return False
    return True

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Check Password Strength")
        print("2. Generate a Strong Password")
        print("3. Quit")

        choice = input("Enter the option (1/2/3): ")

        if choice == '1':
            password = input("Enter a password to check its strength: ")
            if is_strong_password(password):
                print("This is a strong password.")
            else:
                print("This is not a strong password. Please use a stronger password.")

        elif choice == '2':
            password_length = int(input("Enter the length of the password (default is 12): "))
            password = generate_random_password(password_length)
            print(f"Generated Password: {password}")

        elif choice == '3':
            print("Exiting the tool.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
