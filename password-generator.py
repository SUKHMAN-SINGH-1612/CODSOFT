'''
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of thepassword.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.
'''
import string
import random

def password_generator(length=8, upper=True, lower=True, numbers=True, special=True):
    all_characters = ''
    
    if upper:
        all_characters += string.ascii_uppercase
    if lower:
        all_characters += string.ascii_lowercase
    if numbers:
        all_characters += string.digits
    if special:
        all_characters += string.punctuation

    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    if len(all_characters) == 0:
        print("You must include at least one type of characters.")
        return None

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

length = int(input("Enter the desired password length: "))
upper = input("Include uppercase letters? (Y/N): ").lower() == 'y'
lower = input("Include lowercase letters? (Y/N): ").lower() == 'y'
numbers = input("Include numbers? (Y/N): ").lower() == 'y'
special = input("Include special characters? (Y/N): ").lower() == 'y'

password = password_generator(length, upper, lower, numbers, special)
if password:
    print("Generated password: ", password)