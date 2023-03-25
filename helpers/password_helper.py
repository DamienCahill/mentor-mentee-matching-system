import hashlib
import random
import string

def generate_random_password():
    # Define the possible characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(chars) for _ in range(10))
    
    return password

def hash_password_string(password):
    return hashlib.md5(password.encode()).hexdigest()