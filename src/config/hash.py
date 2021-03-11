from decouple import config
import bcrypt

def key(password):
    return bcrypt.kdf(
        password=password.encode('utf8'),
        salt=config('salt').encode('utf8'),
        desired_key_bytes=32,
        rounds=30)

def check(password,hashed):
    return bcrypt.checkpw(key(password), hashed)
def hash(password):
    return bcrypt.hashpw(key(password), bcrypt.gensalt(10))