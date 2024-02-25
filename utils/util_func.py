import hashlib
import os


def hash_password(password: str) -> dict:
    salted = password + os.urandom(16).hex()
    return {
        "password": hashlib.sha256(salted.encode()).hexdigest(),
        "salt": salted,
    }


def generate_jwt_token()