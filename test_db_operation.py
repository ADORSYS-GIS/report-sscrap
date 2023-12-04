import unittest
import sqlite3
import database

class TestDbOpertaions(unittest.TestCase):
    def setUp(self):
        # Connecting to the sqlite database for testing
        self.conn = sqlite3.connect('analysis_results.db')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the database connection after each test
        self.conn.close()
        

    def test_store_in_database(self):
        # Test storing data in the database..
        #expected_data = the analysed_data
        expected_data = [
    {
        'url': 'Test data 1',
        'number_of_text': 'Test data 2',
        'total_text': 'Test data 3',
        'number_of_images': 'Test data 4'
    }
]
        # Store the test data
        database.store_analysis_results_in_database(expected_data)

        # Query the database to check if the data is stored
        self.cursor.execute("SELECT * FROM analysis_results")
        actual_data = self.cursor.fetchall()
        # Convert the actual_data to a list of dictionaries/array of rows columns
        actual_data = [{'url': actual_data[0][1], 'number_of_text': actual_data[0][2], 'total_text': actual_data[0][3], 'number_of_images': actual_data[0][4]}]

        # Assert that the actual_data matches the expected_data
        self.assertEqual(actual_data, expected_data)
        print(actual_data)

if __name__ == '__main__':
    unittest.main()