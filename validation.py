
import csv

def validate_csv_data():
    csv_file = open('blog_scrapped_data.csv', 'r')
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    next(csv_reader)

    for row in csv_reader:
        if len(row) != 1:
            print("Invalid row found in the CSV file:", row)
            return False

    csv_file.close()
    return True

# This will call function
is_valid = validate_csv_data()

if is_valid:
    print("CSV data is valid.")
else:
    print("CSV data is invalid.")
#this is to be ran after the csv file is created 