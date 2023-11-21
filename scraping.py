import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib.error import HTTPError
from urllib.error import URLError

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, "html.parser")
        extracted_data = []
        for element in soup.find_all('p'):
            extracted_data.append(element.text)
        return extracted_data
    
    except requests.HTTPError as e:
        print("HTTP error occurred:")
        print(e)

    except requests.RequestException as e:
        print("An error occurred:")
        print(e)

    except Exception as e:
        print(f"Error scraping website: {url}")
