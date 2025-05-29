import unittest
from app import app

class TodoGameTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post('/add', data=dict(task='Write Code'), follow_redirects=True)
        self.assertIn(b'Write Code', response.data)

if __name__ == '__main__':
    unittest.main()
