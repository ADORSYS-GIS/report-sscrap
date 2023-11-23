import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask, request, jsonify

class FlaskURLTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.driver = webdriver.Chrome()  

        @self.app.route('/save_url', methods=['POST'])
        def scrape():
            urls = request.form.getlist('urls')
            validated_urls = validate_urls(urls)
            if validated_urls:
                return jsonify({'message': 'Scraping in progress...', 'validated_urls': validated_urls}), 200
            else:
                return jsonify({'error': 'Invalid URLs provided.'}), 400

    def tearDown(self):
        self.driver.quit()

    def test_save_url(self):
        self.driver.get('http://localhost:5000') 
        input_element = self.driver.find_element_by_name('urls')
        input_element.send_keys('https:/google.com')
        input_element.send_keys(Keys.RETURN)
        response = self.driver.find_element_by_tag_name('body').text
        self.assertIn('Scraping in progress', response)

if __name__ == '__main__':
    unittest.main()