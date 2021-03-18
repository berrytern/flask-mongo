from decouple import config
from src.config.hash import hash
from collections import OrderedDict
from src.config.db import db
#from collections import OrderedDict
#from src.config.types import BinaryType, NumberType, StringType

import pymongo# Force create!
from pymongo import MongoClient
#  $jsonSchema expression type is prefered.  New since v3.6 (2017):
dados_json = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["username", "password"],
    "properties": {
      "username": {
        "bsonType": "string",
        "description": "Type string requerid"
      },
      "password": {
        "bsonType": "binData",
        "description": "Type string requerid"
      }
    }
  }
}

#db.users.create_index([("username",pymongo.ASCENDING)],unique=True)



class UserModel:
  collection=None

  def __init__(self):
    self.db=db
    if(not 'users' in self.db.list_collection_names()):
      self.db.create_collection('users')
    dados_json = {"$jsonSchema": {"bsonType": "object","required": ["username", "password"],"properties": {"username": {"bsonType": "string","description": "Type string requerid"},"password": {"bsonType": "binData","description": "Type string requerid"}}}}
    analises_schema = dados_json
    dados = [('collMod', 'users'), ('validator', analises_schema),('validationLevel', 'moderate')]
    self.db.command(OrderedDict(dados))
    self.collection = self.db.users
    self.collection.create_index("username",unique=True)

  def find_one(self,username):
    return self.collection.find_one({"username":username})

  def find_all(self,username):
    return self.collection.find({"username":username})
    
  def create(self,username, password):
    return self.collection.insert_one({"username":username,"password":hash(password)})
    
  def update(self,username, password):
    return self.collection.update_one({"username":username},{"$set":{"password":hash(password)}})
    
  def delete(self,username):
    return self.collection.delete_one({"username":username})