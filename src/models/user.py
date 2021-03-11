from decouple import config
from src.config.hash import hash
from src.config.db import db
from collections import OrderedDict
from src.config.types import BinaryType, NumberType, StringType
import sys

db.users  # Force create!

#  $jsonSchema expression type is prefered.  New since v3.6 (2017):
"""vexpr = {"$jsonSchema":
  {
    "bsonType": "object",
    "required": [ "username", "password" ],
    "properties": {
    "username": {
        "bsonType": "string",
        "description": "must be a string and is required"
    },
    "password": {
        "bsonType": "bin",
        "description": "must be a string and is required"
    },  
    }
  }
}

cmd = OrderedDict([('collMod', 'users'),
        ('validator', vexpr),
        ('validationLevel', 'moderate')])

db.command(cmd)
"""
class UserModel():
    @classmethod
    def find_by_username(self,username):
        return db.users.find_one({"username":username})
    @classmethod
    def create(self,username, password):
        return db.users.insert_one({"username":username,"password":hash(password)})
