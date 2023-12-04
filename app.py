from scraping import scrape_website, save_to_csv, clear_csv_file
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import json
import os
from apiendpoint import fetch_data_from_database

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Setting a secret key for flash messages

@app.route("/")
def index():
    return redirect(url_for("index.html"))

@app.route("/input")
def input():
    return render_template("input.html")

# Setting up backend to receive urls
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

# Modified routing based on input fields from the user involving images or number of text
@app.route('/scrape', methods=['POST'])
def scrape_data():
    urls = request.form.get('urls')
    depth = int(request.form.get('depth', 1))

    url_list = [url.strip() for url in urls.split('\n') if url.strip()]

    scraped_data = []

    for url in url_list:
        data = scrape_website(url, depth)
        scraped_data.append(data)

    save_to_csv(scraped_data)

    flash('Scraping and saving to CSV successful!', 'success')

    return render_template('results.html', data=scraped_data)

#API endpoint to fetch analysis result from databse
@app.route('/api/fetch-data', methods=['GET'])
def get_data():
    # Get specified columns from the query parameters
    columns = request.args.getlist('columns')

    # Fetch data based on criteria
    df = fetch_data_from_database(columns=columns)

    # Convert the DataFrame to an HTML table 
    html_table = df.to_html(index=False, classes='table-striped table-bordered')

    # rendering the table
    return render_template('table_template.html', table_content=html_table)

if __name__ == '__main__':
    clear_csv_file()  # Clear the CSV file before running the application
    app.run(debug=True)