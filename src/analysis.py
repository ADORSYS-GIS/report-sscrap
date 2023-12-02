import json
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import csv

#code
def perform_analyses(data_file):
    try:
        # Open file in read mode
        data = 'data.csv'

        with open(data, 'r') as f:
            file_content = f.read()


        # Try to parse as JSON
        try:
            data = json.loads(file_content)
            is_json = True
        except json.JSONDecodeError:
            is_json = False

        # If JSON parsing failed, try parsing as CSV
        if not is_json:
            try:
                # If the file has headers
                data = list(csv.DictReader(StringIO(file_content)))
                is_csv = True
            except csv.Error:
                is_csv = False

        if not is_json and not is_csv:
            raise ValueError("The file format is not supported.")

        if is_json and not isinstance(data, list):
            raise ValueError("The data should be formatted as a list of objects.")

        df = pd.DataFrame(data)

        # Display basic statistics
        print("Total Websites Analyzed:", df.shape[0])
        print("Average character count:", df['char_count'].mean())
        print("Average image count:", df['image_count'].mean())

        # plot character count histogram
        plt.figure(figsize=(10, 5))
        df['char_count'].hist(bins=50)
        plt.title('Character count histogram')
        plt.xlabel('Character count')
        plt.ylabel('Frequency')
        plt.show()

        # plot image count histogram
        plt.figure(figsize=(10, 5))
        df['image_count'].hist(bins=50)
        plt.title('Image count histogram')
        plt.xlabel('Image count')
        plt.ylabel('Frequency')
        plt.show()

    except ValueError as e:
        print(e)

    except FileNotFoundError:
        print("The file was not found")