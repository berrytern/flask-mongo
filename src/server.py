import sys
sys.path[0]=sys.path[0][:sys.path[0].find('/',len(sys.path[0])-6)]
from src.app import app
app.run(host='0.0.0.0',port=3000)
