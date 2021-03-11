from src.config.hash import check
from src.config.auth import encode, decode
from pymongo import I
from time import time
from flask_restful import Resource,reqparse
from src.models.user import UserModel
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
UserModel=UserModel()
class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',required=True)
    parser.add_argument('password',required=True)
        
    def post(self):#login
        args=User.parser.parse_args()
        user=UserModel.find_by_username(args['username'])

        if(not user):
            return "Not Found", 404
        elif(check(args['password'],user['password'])):
            return create_access_token({"username":user['username'],"exp":int(time())+60*6}),200
        else:
            return "Unauthorized",401
    @jwt_required
    def update(self):#altera senha
        User.parser.add_argument('new_password',required=True)
        args=User.parser.parse_args()
        user=UserModel.find_one({'username':args['username']})
        
        if(not user):
            return "Not Found", 404
        elif(check(args['password'],user['password'])):
            user['password']=args['new_password']
            user.save()
            return "Ok",200
        else:
            return "Unauthorized",401

class Register(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',required=True)
    parser.add_argument('password',required=True)

    def post(self):
        args=User.parser.parse_args()
        user=UserModel.find_by_username(args['username'])

        if(not user):
            try:
                UserModel.create(args['username'],args['password'])
                return "Criated", 201
            except ValueError:
                return ValueError,500
        else: 
            return "Exists",409