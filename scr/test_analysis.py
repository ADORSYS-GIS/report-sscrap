import unittest
import pandas as pd
from analysis import perform_analyses

class TestPerformAnalyses(unittest.TestCase):

    def test_perform_analyses_with_json(self):
        # Here, we create a JSON string as an example input
        json_data = """
        [
            {"url": "http://www.alibaba.com", "char_count": 100, "image_count": 2},
            {"url": "http://www.booking.com", "char_count": 200, "image_count": 3}
        ]
        """
        # We save this JSON string to a file
        with open('data.json', 'w') as f:
            f.write(json_data)

        # Now, we call our analysis function with the JSON file
        perform_analyses('data.json')

        # We read the data back from the file to a pandas DataFrame
        df = pd.read_json('data.json')

        # We check if the number of websites analyzed is correct
        self.assertEqual(df.shape[0], 2)

        # We check if the average character count is correct
        self.assertAlmostEqual(df['char_count'].mean(), 150)

        # We check if the average image count is correct
        self.assertAlmostEqual(df['image_count'].mean(), 2.5)

    def test_perform_analyses_with_csv(self):
        # Here, we create a CSV string as an example input
        csv_data =  """ url,char_count,image_count
                        http://www.alibaba.com,100,2
                        http://www.booking.com,200,3
                    """
        # We save this CSV string to a file
        with open('data.csv', 'w') as f:
            f.write(csv_data)

        # Now, we call our analysis function with the CSV file
        perform_analyses('data.csv')

        # We read the data back from the file to a pandas DataFrame
        df = pd.read_csv('data.csv')

        # We check if the number of websites analyzed is correct
        self.assertEqual(df.shape[0], 2)

        # We check if the average character count is correct
        self.assertAlmostEqual(df['char_count'].mean(), 150)

        # We check if the average image count is correct
        self.assertAlmostEqual(df['image_count'].mean(), 2.5)

if __name__ == '__main__':
    unittest.main()