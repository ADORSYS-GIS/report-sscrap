# Code Documentation

## Overview

This module facilitates web scraping using Beautiful Soup and requests. It provides functions to scrape webpages, save scraped data to a CSV file, and read previously saved data. The module is designed to be user-friendly and flexible, allowing customization of scraping parameters.

## Functions

- scrape_website(url, depth=1, specific_data=None): 
  Scrapes a webpage and extracts relevant data based on optional parameters.

- save_scrapped_data(data, filename='scraped_data.csv'):
  Saves the scraped data to a CSV file.

- read_scrapped_data(filename='scraped_data.csv'):
  Reads the previously saved scraped data from a CSV file.

#### Parameters:
- `url` (str): The URL of the webpage to scrape.
- `depth` (int): The depth of recursive scraping. Default is 1 (no recursion).
- `specific_data` (list): List of specific data identifiers to look for in the HTML.

#### Returns:
- `list`: Extracted data from the webpage.

#### Raises:
- `requests.HTTPError`: If an HTTP error occurs.
- `requests.RequestException`: If a general request exception occurs.
- `Exception`: For other unexpected errors.

### 2. `save_scrapped_data(data, filename='scraped_data.csv')`

Saves the scraped data to a CSV file.

#### Parameters:
- `data` (list): The data to be saved.
- `filename` (str): The name of the CSV file. Default is 'scraped_data.csv'.

#### Returns:
- None

#### Raises:
- `Exception`: If an error occurs during data saving.

### 3. `read_scrapped_data(filename='scraped_data.csv')`

Reads the previously saved scraped data from a CSV file.

#### Parameters:
- `filename` (str): The name of the CSV file. Default is 'scraped_data.csv'.

#### Returns:
- `list`: The previously saved data.

#### Raises:
- `Exception`: If an error occurs during data reading.

## Dependencies

- `requests`
- `beautifulsoup4`

## beautifulsoup4
Purpose: Beautiful Soup is a Python library for parsing HTML and XML documents. It provides convenient methods and data structures to extract data from webpages.

## Usage
1. Import the module:
   from web_scraping import scrape_website, save_scrapped_data, read_scrapped_data

2. Scrape a website:
   url = 'https://example.com'
   scraped_data = scrape_website(url)
   print(scraped_data)

3. Save scraped data to a CSV file:
   save_scrapped_data(scraped_data, 'my_data.csv')

4. Read previously saved data from a CSV file:
   previous_data = read_scrapped_data('my_data.csv')
   print(previous_data)

## Conclusion

In conclusion, this web scraping module provides a simple and flexible solution for extracting data from webpages. Leveraging the power of Beautiful Soup and requests, it enables users to scrape content from URLs, customize scraping parameters, and save/read data efficiently. The module's functions are designed to be user-friendly, and the provided example usage demonstrates its practical application.