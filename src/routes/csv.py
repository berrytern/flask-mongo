from config.auth import encode, decode

def csv(request):
    if(request.method == 'GET'):
        print('get')
        token=encode({'method':'GET'})
        return {'encode':token,'decode':decode(token)}