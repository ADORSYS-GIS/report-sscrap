from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
import json
import os
import re
from sklearn.cluster import KMeans

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("input"))

@app.route("/input")
def input():
    return render_template("input.html")

@app.route('/save_url', methods=['POST'])
def save_url():
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
def scrape_data_route():
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

@app.route('/impliment-data-analysis', methods=['GET', 'POST'])
def load_scraped_data(file_path='scraped_data/scraped_data.csv', delimiter='\t'):
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            data = pd.read_csv(file_path, sep=delimiter)

            # Add a placeholder for 'Data' column (replace 'column_name' with the actual column name)
            data['Data'] = 'sample text'

            return data
        else:
            return None
    except pd.errors.EmptyDataError:
        return None

def analyze_data(data):
    if data is not None and 'Data' in data.columns:
        # Calculate average word count and image count
        data['WordCount'] = data['Data'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))
        data['ImageCount'] = data['Data'].apply(count_images)

        # Check if 'WordCount' and 'ImageCount' columns exist in the DataFrame
        if 'WordCount' in data.columns and 'ImageCount' in data.columns:
            average_word_count = data['WordCount'].mean()
            average_image_count = data['ImageCount'].mean()

            return {'average_word_count': average_word_count, 'average_image_count': average_image_count}
        else:
            return None
    else:
        return None

def count_images(text):
    img_tags = re.findall(r'<img[^>]+>', str(text))
    return len(img_tags)

def perform_cluster_analysis(data):
    # Analyze the data
    analysis_result = analyze_data(data)

    # Extract relevant features for clustering
    features = data[['WordCount', 'ImageCount']]

    # Check if there are any samples to cluster
    if not features.empty:
        # Use K-Means clustering
        kmeans = KMeans(n_clusters=3, random_state=42)  
        data['Cluster'] = kmeans.fit_predict(features)

        return data[['Data', 'Cluster']]
    else:
        # Handle the case when there are no samples to cluster
        return None

@app.route('/')
def home():
    # Load the scraped data
    data = load_scraped_data()

    if data is not None:
        # Perform cluster analysis
        cluster_result = perform_cluster_analysis(data)

        if cluster_result is not None:
            # Render the template with the data and analysis result
            return render_template('test.html', data=data.to_html(), analysis_result=None, cluster_result=cluster_result.to_html())
        else:
            # Render the template with the data and analysis result
            return render_template('test.html', data=data.to_html(), analysis_result=None, cluster_result=None)
    else:
        return render_template('test.html', data=None, analysis_result=None, cluster_result=None)

if __name__ == '__main__':
    app.run(debug=True)
