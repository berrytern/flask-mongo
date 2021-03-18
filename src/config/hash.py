from decouple import config
import bcrypt
import base64
import hashlib
def bs64(password):
    return base64.b64encode(hashlib.sha256(password.encode('utf8')).digest())
def key(password):
    return bcrypt.kdf(
        password=password.encode('utf8'),
        salt=config('salt').encode('utf8'),
        desired_key_bytes=32,
        rounds=35)

def check(password,hashed):
    return bcrypt.checkpw(bs64(password), hashed)
def hash(password):
    return bcrypt.hashpw(bs64(password), bcrypt.gensalt(5))