import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect(
    host="your_hostname",
    port="your port",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor
cur = conn.cursor()

# Execute a SQL query
cur.execute("SELECT * FROM your_table")

# Fetch the results
results = cur.fetchall()

# Open a file in the downloads folder
with open("/downloads/output.csv", "w", newline="") as f:
    # Create a CSV writer
    writer = csv.writer(f)

    # Write the column names
    writer.writerow([col[0] for col in cur.description])

    # Write the query results
    writer.writerows(results)

# Close the cursor and connection
cur.close()
conn.close()
