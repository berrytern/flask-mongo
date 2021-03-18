from decouple import config
from flask import Flask
from flask_restful import Api
from src.routes.user import User, Register
from src.routes.csv import Csv
from flask_jwt_extended import JWTManager, get_jwt, get_jwt_identity
import datetime
app=Flask(__name__)
app.config['JWT_SECRET_KEY']=config("secret")
app.config['JWT_TOKEN_LOCATION']="headers"
app.config['JWT_ACCESS_TOKEN_EXPIRES']=datetime.timedelta(minutes=int(config('exp')))
api=Api(app)
jwt=JWTManager(app)

api.add_resource(User,'/login')
api.add_resource(Register,'/register')
api.add_resource(Csv,'/save/csv')