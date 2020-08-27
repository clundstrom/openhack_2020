import hashlib as hl


def registerUser(username, password):
    hash = hl.scrypt()
