import unittest
from app import app

class TestScrapeEndpoint(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_valid_urls(self):
        data = {'urls': ['https://www.google.com', 'https://www.facebook.com']}
        response = self.client.post('/save_url', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Scraping in progress', response.data)

    def test_invalid_urls(self):
        data = {'urls': ['example.com', 'ftp://example2.com']}
        response = self.client.post('/save_url', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid URLs provided', response.data)

if __name__ == '__main__':
    unittest.main()