import jwt

def encode(payload):
    return jwt.encode(payload, "secret", algorithm="HS256")
def decode(token):
    return jwt.decode(token, "secret", algorithms=["HS256"])