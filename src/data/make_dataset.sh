#!/bin/bash

# Define paths to your SQLite database and SQL script
db_path="data/raw/biobio.db"
sql_script_path="src/data/make_csv.sql"

# Define the output CSV file path
output_csv="data/raw/data.csv"

# Run the SQLite3 command to execute the SQL script and save the result as a CSV
sqlite3 -header -csv "$db_path" < "$sql_script_path" > "$output_csv"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "SQLite command completed. Output saved to: $output_csv"
else
    echo "SQLite command failed."
fi