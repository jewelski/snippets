# This code will try to establish a connection with the database, and if it is successful, 
# it will print a message indicating that the connection was established. 
# If there was an error connecting to the database, it will print the error message.

import psycopg2

try:
    # Connect to the database
    conn = psycopg2.connect(
        host="your_host",
        port="your_port",
        user="your_username",
        password="your_password",
        database="your_database"
    )
except psycopg2.Error as e:
    print("Error connecting to the database:")
    print(e)
else:
    print("Connection established successfully")
