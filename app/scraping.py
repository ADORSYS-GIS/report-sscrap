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
        print(e)
    return None

while True:
    url = input("Enter the URL you want to scrape: ")
    extracted_data = scrape_website(url)
    if extracted_data:
        print("Extracted data:")
        for data in extracted_data:
            print(data)
        break
    else:
        print("Error scraping the website. Please try again.")