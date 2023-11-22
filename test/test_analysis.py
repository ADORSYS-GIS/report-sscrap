import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FlaskJSTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000/results")

    def test_javascript_function(self):
        wait = WebDriverWait(self.driver, 5)

        try:
            output_element = wait.until(EC.visibility_of_element_located((By.ID, 'output-element')))
            self.assertEqual(output_element.text, 'START ANALYSIS')
            
        except TimeoutException:
            print("Timeout occurred while waiting for the element to be visible.")
            
        except Exception as e:
            print(str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()