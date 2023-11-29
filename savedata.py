import csv

def save_scrapped_data(data, filename='scraped_data.csv'):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for item in data:
                csv_writer.writerow([item])
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

def read_scrapped_data(filename='scraped_data.csv'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = [line.strip() for line in file.readlines()]
        print(f"Data read from {filename}")
        return data
    except Exception as e:
        print(f"Error reading data: {e}")
        return None


# url = input("Enter the URL you want to scrape: ")
# scraped_data, total_characters = scrape_website(url)
# save_scrapped_data(scraped_data)
# read_data = read_scrapped_data()
