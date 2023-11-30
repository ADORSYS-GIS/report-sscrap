import unittest
from bs4 import BeautifulSoup
import requests


class TestDataSavingUnit(unittest.TestCase):
    def test_extract_and_store_csv(self):
        # Arrange
        source = requests.get('https://webscraper.io/blog').text
        soup = BeautifulSoup(source, 'html.parser')
        expected_output = "CSV file created and data stored successfully."

        # Act
        result = (soup)

        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()