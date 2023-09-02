import hashlib

def generate_hash(val: str):
    #10 rounds :)
    hashgen = hashlib.sha512()
    hashgen.update(str.encode(val))
    return hashgen.hexdigest()