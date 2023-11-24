import csv
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib.error import HTTPError

def scrape_website(url, choice):
    total_characters = 0
    extracted_data = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        if choice == '1':  # User chose to scrape text
            for element in soup.find_all('p'):
                extracted_data.append(element.text)
                total_characters += len(element.text)
        elif choice == '2':  # User chose to scrape images
            for img in soup.find_all('img', src=True):
                extracted_data.append(img['src'])
        else:
            print("Invalid choice. Please enter '1' or '2'.")
            return None

        return extracted_data, total_characters

    except requests.HTTPError as e:
        print("HTTP error occurred:")
        print(e)
    except requests.RequestException as e:
        print("An error occurred:")
        print(e)
    except Exception as e:
        print(f"Error scraping website: {url}")

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for item in data:
            csv_writer.writerow([item])

# Main code
choice = None  # Define choice variable outside the loop
while True:
    url = input("Enter the URL you want to scrape: ")

    print("Choose the type of data to scrape:")
    print("1. Scrape text (displays total characters)")
    print("2. Scrape images")

    user_choice = input("Enter your choice (1 or 2): ")
    choice = user_choice  # Assign user_choice to choice variable

    extracted_data, total_characters = scrape_website(url, choice)

    if extracted_data:
        if choice == '1':
            print(f"Total number of characters: {total_characters}")
        print(f"Number of elements: {len(extracted_data)}")
        print("Extracted data:")
        for data in extracted_data:
            print(data)
        
        # Save the data to a CSV file
        save_to_csv(extracted_data, 'scraped_data.csv')

        print("Data saved to 'scraped_data.csv'")
        break
