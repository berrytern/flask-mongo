from flask import Flask
from flask import request
from src.routes.user import login,register
from src.routes.csv import csv
from src.config.db import db
#print(db.list_collection_names())
#db.insert_one({"algo":'teste'})
app=Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def i_login():
    return login(request,db.users)
@app.route('/register',methods=['GET','POST'])
def i_register():
    return register(request,db.users)