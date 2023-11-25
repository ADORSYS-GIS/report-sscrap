import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib.error import HTTPError, URLError
import csv
def scrape_website(url):
    total_characters = 0
    extracted_data = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        for element in soup.find_all('p'):
            extracted_data.append(element.text)
            total_characters += len(element.text)

        for img in soup.find_all('img', src=True):
            extracted_data.append(img['src'])

        return extracted_data, total_characters

    except requests.HTTPError as e:
        print("HTTP error occurred:")
        print(e)
    except requests.RequestException as e:
        print("An error occurred:")
        print(e)
    except Exception as e:
        print(f"Error scraping website: {url}")


def save_scrapped_data(data, filename='scraped_data.csv'):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for item in data:
                csv_writer.writerow([item])
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def read_scrapped_data(filename='scraped_data.csv'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = [line.strip() for line in file.readlines()]
        print(f"Data read from {filename}")
        return data
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

# Example usage:
url = input("Enter the URL you want to scrape: ")
scraped_data, total_characters = scrape_website(url)
save_scrapped_data(scraped_data)
read_data = read_scrapped_data()
