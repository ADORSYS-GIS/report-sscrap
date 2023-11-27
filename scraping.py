import requests
from bs4 import BeautifulSoup
import csv
import re  # Import the regular expression module

def scrape_website(url, depth):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize lists to store data from all pages
        data_text = []
        data_images = []

        # Loop through all pages up to the specified depth
        for _ in range(depth):
            # Extract text data
            data_text += [p.text for p in soup.find_all('p')]

            # Extract image data
            data_images += [img['src'] for img in soup.find_all('img')]

            # Check if there is a next page link
            next_page_link = soup.find('a', {'class': 'next-page-link'})
            if next_page_link:
                next_page_url = next_page_link['href']
                response = requests.get(next_page_url)
                soup = BeautifulSoup(response.text, 'html.parser')
            else:
                # Break the loop if there is no next page
                break

        # Combine text into a single string and count words
        total_text = ' '.join(data_text)
        total_text_word_count = len(re.findall(r'\b\w+\b', total_text))

        return {'url': url, 'text': data_text, 'total_text': total_text, 'total_text_word_count': total_text_word_count, 'images': data_images}
    except Exception as e:
        print(f"Error scraping data from {url}: {e}")
        return {'url': url, 'text': [], 'total_text': '', 'total_text_word_count': 0, 'images': []}

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['url', 'number of text in website', 'total text word count', 'images found in website'])

        for item in data:
            csv_writer.writerow([item['url'], len(item['text']), item['total_text_word_count'], len(item['images']), item['images']])

# Additional function for testing purposes only
def clear_csv_file():
    open('scraped_data.csv', 'w').close()