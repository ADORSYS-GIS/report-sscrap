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

def store_analysis_results_in_database(results):
    # Create the database schema if it doesn't exist
    create_database_schema()

    connection = sqlite3.connect('analysis_results.db')
    cursor = connection.cursor()

    try:
        for result in results:
            cursor.execute('''
                INSERT INTO analysis_results (url, number_of_text, total_text, number_of_images)
                VALUES (?, ?, ?, ?)
            ''', (result['url'], result['number_of_text'], result['total_text'], result['number_of_images']))
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        connection.commit()
        connection.close()