from flask_jwt_extended import jwt_required
from flask_restful import Resource,reqparse
import pandas as pd
from src.config.db import db

def get_domain(link):
    domain=link[:link.find('/',link.find('.'))]
    if(domain.find('.')!=-1):
        domain=domain[domain.find('/')+2:]
    return domain
class Csv(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('link',required=True)
    parser.add_argument('delimiter',required=True)
    parser.add_argument('name',required=True)
    parser.add_argument('skiprows')
    
    @jwt_required()    
    def post(self):#login
        args=Csv.parser.parse_args()
        #https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv
        link, delimiter, name, skiprows= args['link'],args['delimiter'], args['name'],args['skiprows']
        get_domain(link)
        try:
            df=pd.read_csv(filepath_or_buffer=link,delimiter=delimiter,skiprows=skiprows)
            if(not name in db.list_collection_names()):
                db.create_collection(name)
                for index, row in df.iterrows():
                    document={}
                    for column in df.columns:
                        document[column]=row[column]
                    db[name].insert_one(document)
                return "Ok",200
            else:
                return "name already exists", 409
        except:
            return args,400