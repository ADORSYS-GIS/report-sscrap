from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class FlaskJSTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000/')

    def test_javascript_function(self):
        # Wait for the element with the ID 'mybutton' to become available
        wait = WebDriverWait(self.driver, 60)
        trigger_button = wait.until(EC.presence_of_element_located((By.ID, 'mybutton')))

        # Click the trigger button
        trigger_button.click()

        # Wait for the output element with the ID 'output-element' to become available
        output_element = wait.until(EC.presence_of_element_located((By.ID, 'output-element')))

        # Verify that the output element's text is as expected
        self.assertEqual(output_element.text, 'JavaScript function executed successfully!')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()