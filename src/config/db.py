from decouple import config
from pymongo import MongoClient
client = MongoClient(config('Mongo_Path'))
db=client.CSVs
