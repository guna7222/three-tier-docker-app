from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import psycopg2.extras
from psycopg2 import OperationalError
import time

app = Flask(__name__)
CORS(app)

# DB config
DB_SETTINGS = {
    "host": "db",
    "database": "cruddb",
    "user": "postgres",
    "password": "postgres"
}

# Retry logic for initial connection check
max_retries = 10
for attempt in range(max_retries):
    try:
        test_conn = psycopg2.connect(**DB_SETTINGS)
        test_conn.close()
        print("Connected to the database.")
        break
    except OperationalError as e:
        print(f"Database not ready, retrying in 2 seconds... ({attempt + 1}/{max_retries})")
        time.sleep(2)
else:
    print("Could not connect to the database after several attempts.")
    exit(1)

# Helper function to get a connection with DictCursor
def get_db_connection():
    return psycopg2.connect(**DB_SETTINGS, cursor_factory=psycopg2.extras.RealDictCursor)

# CRUD Routes

@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items ORDER BY id;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING *;", (name,))
    new_item = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE items SET name = %s WHERE id = %s RETURNING *;", (name, item_id))
    updated_item = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if updated_item:
        return jsonify(updated_item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = %s RETURNING id;", (item_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if deleted:
        return jsonify({'message': 'Deleted successfully'})
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
