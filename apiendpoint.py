import pandas as pd
import sqlite3

DATABASE = 'analysis_results.db'

def fetch_data_from_database(columns):
    # Default columns to fetch 
    columns = ["url", "number_of_text", "total_text", "number_of_images"]
   
    # Create a comma-separated string of column names for the SELECT statement
    columns_str = ", ".join(columns)

    # Construct the SQL query
    sql_query = f"SELECT {columns_str} FROM analysis_results"

    # Execute the query
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(sql_query)

    # Fetch all the results
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(data, columns=columns)

    return df
