from flask import Flask, render_template, redirect, url_for, request, session, flash
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import json
from sscrapy import extract_and_store_csv
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return redirect(url_for("input"))

@app.route("/input")
def input():
	return render_template("input.html")

@app.route("/sscrapy")
def extract_csv():
	source = requests.get('https://webscraper.io/blog').text
	soup = BeautifulSoup(source, 'lxml')
	return extract_and_store_csv(soup)	

@app.route("/results")
def results():
	return render_template("results.html")

if __name__ == '__main__':
	app.run(debug=True)
