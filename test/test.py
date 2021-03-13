import sys
sys.path[0]=sys.path[0][:sys.path[0].find('/',len(sys.path[0])-6)]
import unittest
from src.app import app

class TestUser(unittest.TestCase):

    def test_register(self):
        test = app.test_client()
        response = test.post('/register')
        print('response: ',response)
        self.assertEqual(400, response.status_code)

if __name__ == '__main__':
    unittest.main()