from flask_jwt_extended import jwt_required
from flask_restful import Resource,reqparse
import pandas as pd

def get_domain(link):
    domain=link[:link.find('/',link.find('.'))]
    if(domain.find('.')!=-1):
        domain=domain[domain.find('/')+2:]
    return domain
        
    def post(self):#login
        args=User.parser.parse_args()
class Csv(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('link',required=True)
    parser.add_argument('name',required=True)
    
    @jwt_required    
    def post(self):#login
        args=User.parser.parse_args()
        #https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv
        link,token, name = args['link'],args['token'], args['name']
        db.get_domain(link)
        pd.read_csv()
        return request.json,200