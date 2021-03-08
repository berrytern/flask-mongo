from decouple import config
from flask import Flask
from flask import request
from routes.login import login
from routes.csv import csv
from pymongo import MongoClient
#c = MongoClient()
#print(c.test_database)
client = MongoClient(config('Mongo_Path'))
db=client.Loja
db.product.insert_one({})

app=Flask(__name__)

@app.route('/login',methods=['GET'])
def i_login():
    return login(request)
@app.route('/csv',methods=['GET','POST'])
def csv():
    return csv()