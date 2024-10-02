import pandas as pd
import mysql.connector
from mysql.connector import Error

# Define your database connection parameters
db_config = {
    'host': 'localhost',
    'database': 'courses',
    'user': 'root',
    'password': 'YES',
    'port': 3307
}

# Read the CSV file into a DataFrame
csv_file_path = '/home/lace/Downloads/courses.csv'
data = pd.read_csv(csv_file_path)

# Option 1: Fill NaN values with an empty string
data.fillna('', inplace=True)

# Print column names to verify
print("DataFrame columns:", data.columns.tolist())

# Print the number of rows read from the CSV
print(f"Number of rows in DataFrame: {len(data)}")
print("DataFrame columns:", data.columns.tolist())

# Function to create the MySQL table
def create_table_if_not_exists():
    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()
            # SQL statement to create a table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS courses (
                Dept VARCHAR(50),
                Course_Number VARCHAR(50),
                Level VARCHAR(50),
                Hours INT,
                Name VARCHAR(255),
                Description TEXT
            )
            '''
            cursor.execute(create_table_query)
            print("Table 'courses' created or already exists.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Function to insert data into MySQL
def insert_data_to_mysql(data):
    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()
            for index, row in data.iterrows():
                sql = "INSERT INTO courses (Dept, Course_Number, Level, Hours, Name, Description) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (row['Dept'], row['Course Number'], row['Level'], row['Hours'], row['Name'], row['Description']))
            connection.commit()
            print(f"Inserted {cursor.rowcount} rows into the database.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Create the table if it doesn't exist
create_table_if_not_exists()

# Call the function to insert data
insert_data_to_mysql(data)
