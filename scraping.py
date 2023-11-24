import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, depth, data_type):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if data_type == 'text':
            data_text = [p.text for p in soup.find_all('p')[:depth]]
            total_text = ' '.join(data_text)  # Combine text into a single string
            data_images = []  # Initialize as empty for 'text' data type
        elif data_type == 'images':
            data_images = [img['src'] for img in soup.find_all('img')[:depth]]
            data_text = []  # Initialize as empty for 'images' data type
            total_text = ''  # Initialize as empty for 'images' data type
        else:
            data_text = []
            data_images = []
            total_text = ''

        return {'url': url, 'text': data_text, 'total_text': total_text, 'images': data_images}
    except Exception as e:
        print(f"Error scraping data from {url}: {e}")
        return {'url': url, 'text': [], 'total_text': '', 'images': []}

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['url', 'number of text in website', 'total text', 'images found in website'])

        for item in data:
            csv_writer.writerow([item['url'], len(item['text']), len(item['total_text']), len(item['images'])])

# Additional function for testing purposes only
def clear_csv_file():
    open('scraped_data.csv', 'w').close()



