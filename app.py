from flask import Flask, jsonify, request, render_template
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    db_path = os.path.join(app.root_path, 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category', 'All')
    conn = get_db_connection()
    if category == 'All':
        products = conn.execute('SELECT * FROM products').fetchall()
    else:
        products = conn.execute('SELECT * FROM products WHERE category = ?', (category,)).fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    category = data['category']
    price = data['price']
    image_url = data.get('image_url', '')
    description = data.get('description', '')
    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, category, price, image_url, description) VALUES (?, ?, ?, ?, ?)',
                 (name, category, price, image_url, description))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added successfully'}), 201

@app.route('/api/delete-product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)