# creating the database schema > database.py
import sqlite3

def create_database_schema():
    connection = sqlite3.connect('analysis_results.db')
    cursor = connection.cursor()

    # Create a table to store analysis results
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            number_of_text INTEGER,
            total_text TEXT,
            number_of_images INTEGER
        )
    ''')

    connection.commit()
    connection.close()