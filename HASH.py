
import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)  # 16 bytes of random salt
    salted_pass = password.encode() + salt
    hash_val = hashlib.sha256(salted_pass).hexdigest()
    return salt.hex(), hash_val

user_password = input("Enter your password: ")

salt, hashed = hash_password(user_password)

print("Salt:", salt)
print("Hashed Password:", hashed)
