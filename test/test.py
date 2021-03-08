import unittest
from routes.routes import app


class TestHome(unittest.TestCase):

    def test_get(self):
        test = app.test_client()
        response = test.get('/login')
        print('response: ',response)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()