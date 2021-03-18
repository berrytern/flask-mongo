from src.config.hash import check
from flask_restful import Resource,reqparse
from src.models.user import UserModel
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
UserModel=UserModel()
class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('password',required=True)
    parser.add_argument('username')
    parser.add_argument('new_password')
    
    def post(self):#login
        args=User.parser.parse_args()
        user=UserModel.find_one(args['username'])

        if(not user):
            return "Not Found", 404
        elif(check(args['password'],user['password'])):
            return create_access_token(identity=user['username']),200
        else:
            return "Unauthorized",401
    
    @jwt_required()
    def put(self):#altera senha
        args=self.parser.parse_args()
        user=UserModel.find_one(get_jwt_identity())
        if(not user):
            return "Not Found", 404
        elif(check(args['password'],user['password'])):
            UserModel.update(get_jwt_identity(),args['new_password'])
            return "Ok",200
        else:
            return "Unauthorized",401
    
    @jwt_required()
    def delete(self):
        args=User.parser.parse_args()
        user=UserModel.find_one(get_jwt_identity())

        if(not user):
            return "Not Found", 404
        elif(check(args['password'],user['password'])):
            if(UserModel.delete(user.username)):
                return "Deleted",200
            else:
                return "not Deleted",500
class Register(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',required=True)
    parser.add_argument('password',required=True)

    def post(self):
        args=User.parser.parse_args()
        user=UserModel.find_one(args['username'])

        if(not user):
            try:
                UserModel.create(args['username'],args['password'])
                return "Criated", 201
            except ValueError:
                return ValueError,500
        else: 
            return "Exists",409