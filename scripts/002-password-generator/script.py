import string 
import secrets 
import re

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(secrets.choice(characters) for i in range(16))

print(password)

def is_strong(pw):  # Simple function to check the password strength and return true or false
    return (
        len(pw) >= 12 and 
        bool(re.search(r'[A-Z]', pw)) and 
        bool(re.search(r'[a-z]', pw)) and
        bool(re.search(r'\d', pw)) and
        bool(re.search(r'[^A-Za-z0-9]', pw))
    )   

print(is_strong(password))