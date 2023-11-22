import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_full_flow(self):
        # Simulate user input for the URL
        user_input_url = input("Enter the website URL: ")

        # Input Webpage URLs
        url_input = self.driver.find_element_by_name('url')
        url_input.send_keys(user_input_url)  # Use user input URL

        depth_input = self.driver.find_element_by_name('depth')
        depth_input.send_keys('1')

        data_select = self.driver.find_element_by_name('data_to_look_for')
        data_select.send_keys('python') 

        scrape_button = self.driver.find_element_by_css_selector('.input-form button')
        scrape_button.click()

        # Wait for the results page to load
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.results ul li')))

        # Verify the scraped data on the results page
        scraped_data = self.driver.find_elements_by_css_selector('.results ul li')
        self.assertTrue(scraped_data)  

if __name__ == '__main__':
    unittest.main()
