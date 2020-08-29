import hashlib
import os


def hash_password(password):
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    ).hex()
    salt = salt.hex()
    hash = hash + salt
    print('Generated hash: ', hash)

    return hash


def is_valid_login(password, old_hash):
    salt = bytes.fromhex(old_hash[-64:])
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    ).hex()
    new_hash = new_hash + salt.hex()

    return new_hash == old_hash
