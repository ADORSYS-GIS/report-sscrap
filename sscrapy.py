from bs4 import BeautifulSoup
import requests
import csv
#from function.csv_json import extract_and_store_csv, extract_and_store_json
def extract_and_store_csv(soup):
    csv_file = open('blog_scrapped_data.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Date Published', 'Category', 'Summary'])

    for article in soup.find_all('div', class_='col-lg-8'):
        p_tags = article.find_all('p')

        headline = article.a.text
        date_published = article.p.text

        if len(p_tags) >= 2:
            second_p_text_category = p_tags[1].get_text(strip=True)
            third_p_text_summary = p_tags[2].get_text(strip=True)

        csv_writer.writerow([headline, date_published, second_p_text_category, third_p_text_summary])

    csv_file.close()
