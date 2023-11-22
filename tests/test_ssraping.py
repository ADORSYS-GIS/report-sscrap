import unittest
from unittest.mock import patch, Mock
from scraping import scrape_website
import requests

class TestScraping(unittest.TestCase):

    def input_url(self):
        return input("Enter the website URL: ")

    @patch('builtins.input', side_effect=['http://example.com'])
    @patch('requests.get')
    def test_successful_scrape(self, mock_requests_get, mock_input):
        
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = '<html><body><p>Test content</p></body></html>'
        mock_requests_get.return_value = mock_response

        # Act
        result = scrape_website(self.input_url())

        # Assert
        self.assertEqual(result, ['Test content'])

    @patch('builtins.input', side_effect=['http://example.com'])
    @patch('requests.get', side_effect=requests.HTTPError('HTTP Error'))
    def test_http_error(self, mock_requests_get, mock_input):
        # Act
        result = scrape_website(self.input_url())

        # Assert
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['http://example.com'])
    @patch('requests.get', side_effect=requests.RequestException('Request Exception'))
    def test_request_exception(self, mock_requests_get, mock_input):
        # Act
        result = scrape_website(self.input_url())

        # Assert
        self.assertIsNone(result)

    @patch('builtins.input', side_effect=['http://example.com'])
    @patch('requests.get', side_effect=Exception('Some Other Exception'))
    def test_other_exception(self, mock_requests_get, mock_input):
        # Act
        result = scrape_website(self.input_url())

       
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()