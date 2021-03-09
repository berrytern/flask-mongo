import sys
sys.path[0]=sys.path[0][:sys.path[0].find('/',len(sys.path[0])-6)]
from src.routes.routes import app
app.run(port=3000)
