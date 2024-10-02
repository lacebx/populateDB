# CSV to MySQL Data Insertion

This Python script reads course data from a CSV file and inserts it into a MySQL database. It's designed to help users easily populate a database with data structured in a CSV format.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- MySQL Server
- Required Python packages: `pandas`, `mysql-connector-python`

You can install the necessary Python packages using pip:

```bash
pip install pandas mysql-connector-python

## CSV File Format

The script expects the CSV file to have the following structure:
Dept	Course Number	Level	Hours	Name	Description
ACCT	ACCT-0010	0	0	Accounting Lower Division	
...	...	...	...	...	...

Make sure your CSV file is properly formatted and saved.

## Database Configuration

Update the database connection parameters in the script:

python

db_config = {
    'host': 'localhost',
    'database': 'courses',
    'user': 'root',
    'password': 'YOUR_PASSWORD',
    'port': 3307
}

Ensure the courses database exists and contains a table named courses with the appropriate columns:

sql

CREATE TABLE courses (
    Dept VARCHAR(50),
    Course_Number VARCHAR(50),
    Level INT,
    Hours VARCHAR(50),
    Name VARCHAR(100),
    Description TEXT
);

## Usage

    Place your CSV file in an accessible location and update the csv_file_path variable in the script to point to the CSV file.

    Run the script:

bash

python3 pop.py

    The script will read the CSV file and insert the data into the MySQL database. You will see output indicating the number of rows inserted.

## Error Handling

If there are any issues during insertion (e.g., data type mismatches), the script will print an error message to help you troubleshoot.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

sql


### Next Steps

1. **Create the `README.md` file**: Save the above content into a file named `README.md` in your project directory.

2. **Update Any Details**: Make sure to replace `YOUR_PASSWORD` with your actual MySQL password in the configuration section.

3. **Add License**: If you want to include a license, create a `LICENSE` file in your project directory as well.

Feel free to modify any sections to better fit your project or add any additional information that might be useful for users! Let me know if you need anything else!
