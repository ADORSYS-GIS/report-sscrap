from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("index.html"))

@app.route("/input")
def input():
    return render_template("input.html")

#setting up backend to receive urls
@app.route('/save_url', methods=['POST'])
def scrap():
    urls = request.form.getlist('urls')
    validated_urls = validate_urls(urls)
    
    if validated_urls:
        return jsonify({'message': 'Scraping in progress...', 'validated_urls': validated_urls}), 200
    else:
        return jsonify({'error': 'Invalid URLs provided.'}), 400

def validate_urls(urls):
    validated_urls = []
    
    for url in urls:
        if url.startswith('http://') or url.startswith('https://'):
            validated_urls.append(url)
    
    return validated_urls


@app.route("/results")
def results():
    return render_template("results.html")

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    depth = int(request.form.get('depth', 1))
    data_to_look_for = request.form.get('data_to_look_for', '')

    # Scrape data from the provided URL
    scraped_data = scrape_data(url, depth, data_to_look_for)

    # Save scraped data to CSV and JSON files
    save_to_csv(scraped_data)
    save_to_json(scraped_data)

    return render_template('results.html', data=scraped_data)

def scrape_data(url, depth, data_to_look_for):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Implementing logic to extract relevant data from the BeautifulSoup object
        scraped_data = extract_data(soup, depth, data_to_look_for)
        return scraped_data
    except requests.exceptions.RequestException as e:
        print(f"Error during scraping: {e}")
        return None

def extract_data(soup, depth, data_to_look_for):
    # Implementing logic to extract data here
    paragraphs = soup.find_all('p')
    scraped_data = [p.text.strip() for p in paragraphs]
    return scraped_data[:depth]

def save_to_csv(data):
    directory = 'scraped_data'
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist

    with open(os.path.join(directory, 'scraped_data.csv'), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Data'])
        for item in data:
            writer.writerow([item])

def save_to_json(data):
    directory = 'scraped_data'
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist

    with open(os.path.join(directory, 'scraped_data.json'), 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

@app.route('/api/start-analysis', methods = ['GET', 'POST'])
def analysis():
	return render_template('test.html')

if __name__ == '__main__':
	app.run(debug=True)