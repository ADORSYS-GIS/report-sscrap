from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
	return redirect(url_for("input"))

@app.route("/input")
def input():
	return render_template("input.html")

#setting up backend to receive urls
@app.route('/scrape', methods=['POST'])
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


@app.route("/results")
def results():
	return render_template("results.html")

if __name__ == '__main__':
	app.run(debug=True)