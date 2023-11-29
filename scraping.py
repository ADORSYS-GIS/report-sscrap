import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib.error import HTTPError, URLError

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
       
        
