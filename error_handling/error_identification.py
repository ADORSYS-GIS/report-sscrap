import requests
from bs4 import BeautifulSoup

def check_network_errors(url):
    try: 
        response = requests.get(url)
        response.raise_for_status()
        print("Network connection is working fine.")
    except requests.exceptions.RequestException as err:
        print("Network connection error:", err)

def check_input_errors(url, input_selector):
    try: 
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        inputs = soup.select(input_selector)

        if not inputs:
            print("No input elements found for the given selector.")
        else:
            for input_element in inputs:
                if 'error' in input_element.get('class', ''):
                    print("Input error detected:", input_element)
                else: 
                    print("Input element is fine:", input_element)
    except requests.exceptions.RequestException as err:
        print ("Network connection error parsing HTML:", err)

