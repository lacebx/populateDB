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

# Call the function to insert data
insert_data_to_mysql(data)
