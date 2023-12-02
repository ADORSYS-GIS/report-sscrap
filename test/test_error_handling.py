import requests
import sqlite3
from sqlite3 import Error as SQLiteError

#identifying network issues
def check_network_errors(urls):
    try: 
        response = requests.get(urls)
        response.raise_for_status()
        print("Network connection is working fine.")
    except requests.exceptions.RequestException as err:
        print("Network connection error:", err)

#identifying database errors 

try:
    connection = sqlite3.connect("analysis_results.db")
    # Continue with the code
except SQLiteError as e:
    print("Error connecting to the database. Please contact support or verify input data.")
    # Handle the error gracefully

def validate_urls(urls):
    validated_urls = []
    for url in urls:
        if not url.startswith(('http://', 'https://')):
            return None

        validated_urls.append(url)