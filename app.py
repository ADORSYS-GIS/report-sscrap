from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import json
from resource.scraping import extract_and_store_csv
import requests
import csv
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("input"))

@app.route("/input")
def input():
    return render_template("input.html")

if __name__ == '__main__':
	app.run(debug=True)
