import mysql.connector
from mysql.connector import Error
import os

def get_db_connection():
    """Create and return a connection to the MySQL database."""
    try:
        # Using environment variables for security (recommended)
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'mysql'),  # Default to 'mysql' (docker container name)
            user=os.getenv('MYSQL_USER', 'root'),  # Default to 'root'
            password=os.getenv('MYSQL_PASSWORD', 'my-secret-pw'),  # Default password
            database=os.getenv('MYSQL_DATABASE', 'testdb')  # Default database
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
