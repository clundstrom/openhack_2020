import hashlib
import os


def hash_password(password):
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000  # It is recommended to use at least 100,000 iterations of SHA-256
    ).hex()
    salt = salt.hex()
    hash = hash + salt
    print('Generated hash: ', hash)

    is_valid_login('12345', hash)
    return hash


def is_valid_login(password, old_hash):
    salt = bytes.fromhex(old_hash[-64:])
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000  # It is recommended to use at least 100,000 iterations of SHA-256
    ).hex()
    new_hash = new_hash + salt.hex()

    return new_hash == old_hash
