from src.config.auth import encode, decode

def csv(request):
    if(request.method == 'GET'):
        print('get')#https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv
        token=encode({'method':'GET'})
        return {'encode':token,'decode':decode(token)}