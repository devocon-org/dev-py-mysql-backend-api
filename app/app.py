# app/app.py
from flask import Flask, jsonify
from dbconnection import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

@app.route('/data')
def data():
    # Get DB connection
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_table')
        rows = cursor.fetchall()
        conn.close()  # Always close the connection
        return jsonify(rows)
    else:
        return jsonify(error="Database connection failed"), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
