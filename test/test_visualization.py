import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GraphTest(unittest.TestCase):

    def tearDown(self):
        self.driver.quit()

    def test_responsive_graph(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000/chart')
        self.driver.maximize_window()
        # Locate the graph element
        graph_element = self.driver.find_element(By.XPATH, "//canvas[@id='myChart2']")
        
        # Get the initial size of the graph element
        initial_size = graph_element.size
        time.sleep(5)
        
        # Resize the browser window to a smaller width
        self.driver.set_window_size(576, self.driver.get_window_size().get('height'))
        time.sleep(3)
        
        self.driver.set_window_size(768, self.driver.get_window_size().get('height'))
        time.sleep(3)
        
        # Get the new size of the graph element after resizing
        resized_size = graph_element.size
        
        # Assert that the graph has resized and its new size is smaller than the initial size
        self.assertLess(resized_size['width'], initial_size['width'])
    
    def test_chart_accuracy(self):
        self.driver = webdriver.Chrome()
        # parsing the url of the chart page
        self.driver.get('http://127.0.0.1:5000/chart')
        time.sleep(3)
        
        # Getting the title of the webpage
        actual_result = self.driver.title
        
        # Expected title or result
        expected_result = '- GIS'
        
        # Testing if the title of the chart page matches
        self.assertEqual(actual_result, expected_result)
        
        # Getting the path of the plot
        graph_element = self.driver.find_element(By.XPATH, "//canvas[@id='myChart2']")
        time.sleep(3)
        # Verifying if the element is displayed on the web page
        self.assertTrue(graph_element.is_displayed)

if __name__ == '__main__':
    unittest.main()
