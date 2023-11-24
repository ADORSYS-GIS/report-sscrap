from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import json
import os
# app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from scraping import scrape_website, save_to_csv, clear_csv_file

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Setting a secret key for flash messages

@app.route("/")
def index():
    return redirect(url_for("input"))

@app.route("/input")
def input():
    return render_template("input.html")

#setting up backend to receive urls
@app.route('/save_url', methods=['POST'])
def scrape():
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
    data_type = request.form.get('data_type', 'text')

    url_list = [url.strip() for url in urls.split('\n') if url.strip()]

    scraped_data = []

    for url in url_list:
        data = scrape_website(url, depth, data_type)
        scraped_data.append(data)

    save_to_csv(scraped_data)

    flash('Scraping and saving to CSV successful!', 'success')

    return render_template('results.html', data=scraped_data)

if __name__ == '__main__':
    clear_csv_file()  # Clear the CSV file before running the application
    app.run(debug=True)
