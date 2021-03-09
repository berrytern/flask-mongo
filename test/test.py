import sys
sys.path[0]=sys.path[0][:sys.path[0].find('/',len(sys.path[0])-6)]
import unittest
from src.routes.routes import app

class TestHome(unittest.TestCase):

    def test_get(self):
        test = app.test_client()
        response = test.get('/login')
        print('response: ',response)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()