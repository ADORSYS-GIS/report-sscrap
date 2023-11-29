Designing a Database Schema 

## Prerequisites:   
    With the basic knowledge in python, you'll need to install the appporaite database management system (e.g., SQLALchemy for MySQL or PostgreSQL). We will be using the sqlite3 db model

- Install the Required Libraries:
    Use pip, the python package manager, to install the necessary libraries. e.g.,
      ```
        pip install SQALchemy
      ```

- Import the Required Libraries:
    In your python script or module, import the necessary libraries for database interaction.
    ```
    import sqlite3
    ```

- Create a Database Connection:
    Establish a connection to your database using the appropraite database URL or connection parameters. This step may vary depending on the DBMS you are using. Below is an example using SQLALchemy with MySQL
      ```
        connection = sqlite3.connect('analysis_results.db')
    cursor = connection.cursor()

      ```

- Define a Base Model:
    Create a base model class using the declarative_base() function provided by SQLAlchemy.This base class will serve as the parent for your table models, e.g,. 
    
     ```python
      Base = declarative_base()
     ```

- Define Tables Models:
    Create python classes that present your database tables. Each class should inherit from the base model( Base ) and define the table name, columns, and their respective data type. Use SQLALchemy's Column class to define columns.

    ```
    cursor.execute(
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            number_of_text INTEGER,
            total_text TEXT,
            number_of_images INTEGER
        )
    )
    ```

### Conclusion
This documentation provided a step-by-step guide on on how we set up our designing a database schema with Python.The create_database_schema function is responsible for creating the SQLite database file (analysis_results.db) and designing the schema for storing analysis results.
It creates a table named analysis_results with columns for id (primary key), url, number_of_text, total_text, and number_of_images
