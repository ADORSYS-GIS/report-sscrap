import sqlite3
import unittest
from refresh import *

# creating the database
def read_database():

    # connect to database
    conn = sqlite3.connect('analysis_results.db')

    # create a cursor element which will permit us execute cursor methods
    cursor = conn.cursor()

    # retrieving the data from the database
    sql = "SELECT * FROM analysis_results"
    cursor.execute(sql)
    data_in_database = cursor.fetchall()

    # commit the changes
    conn.commit()
    add_primary_key_query = 'CREATE UNIQUE INDEX id ON analysis_results();'
    conn.execute(add_primary_key_query)
    return data_in_database

# creating a test class which inherits from the unitest.Testcase
class TestDataRefresh(unittest.TestCase):

 # define a test method to test the data refresh functionality
 def testNewdata(self):

     expected_result = read_database()

     actual_result = latest_data

     # test if actual result is equal to the expected result
     self.assertEqual(actual_result, expected_result)

# run test
if __name__ == '__main__':
    unittest.main()






