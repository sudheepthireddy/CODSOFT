import random
import string
def generate_password(length):
    """Generate a random password of specified length."""
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
