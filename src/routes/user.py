from src.config.hash import hash, check
from src.config.auth import encode, decode
from time import time


def login(request,users):
    if(request.method == 'POST'):
        if(not 'username' in request.json or not 'password' in request.json):
            return 'Missing Fields',400
        elif(not isinstance(request.json['password'], str) or not isinstance(request.json['username'], str)):
            return "password and username must be string",400
        elif(users.find_one({'username':request.json['username']})==None):
            return "Not Found", 404
        else:
            user=users.find_one({'username':request.json['username']})
            if(check(request.json['password'],user['password'])):
                return encode({"username":user['username'],"exp":int(time())+60*1}),200
            else:
                return "Unauthorized",401
    if(request.method == 'GET'):
        return "get",200

def register(request,users):
    if(request.method == 'POST'):
        if(not 'username' in request.json or not 'password' in request.json):
            return 'Missing Fields',400
        if(not isinstance(request.json['password'], str)):
            return "password must be string",400
        elif(users.find_one({'username':request.json['username']})==None):
            users.insert_one({"username":request.json['username'],"password":hash(request.json['password'])})
            return "Criated", 201
        else: 
            return "Exists",409