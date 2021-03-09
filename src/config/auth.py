from decouple import config
import jwt

def encode(payload):
    return jwt.encode(payload, config("secret"), algorithm="HS256")
def decode(token):
    return jwt.decode(token, config("secret"), algorithms=["HS256"])