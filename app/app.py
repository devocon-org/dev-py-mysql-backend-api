# app/app.py
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='mysql',  # The MySQL container name
        user='root',
        password='my-secret-pw',
        database='testdb'
    )

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

@app.route('/data')
def data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
