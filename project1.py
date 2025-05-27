import random
import string

def generate_password(min_length, use_numbers=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Build the pool of characters
    characters = letters
    if use_numbers:
        characters += digits
    if use_special:
        characters += special

    while True:
        password = ''.join(random.choice(characters) for _ in range(min_length))

        # Validation checks
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in special for c in password)

        if has_upper and has_lower:
            if (not use_numbers or has_digit) and (not use_special or has_special):
                return password

# Input from user
min_length = int(input("Enter the minimum password length: "))
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and display password
password = generate_password(min_length, include_numbers, include_special)
print("Generated password:", password)
