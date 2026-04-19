import sqlite3
import os

def init_db():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            image_url TEXT,
            description TEXT
        )
    ''')
    # Insert sample data
    sample_products = [
        ('Wireless Headphones', 'Electronics', 2999.00, 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop', 'High-quality wireless headphones with noise cancellation.'),
        ('Smartphone Case', 'Accessories', 499.00, 'https://images.unsplash.com/photo-1556656793-08538906a9f8?w=500&h=500&fit=crop', 'Protective case for smartphones.'),
        ('Running Shoes', 'Footwear', 2499.00, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop', 'Comfortable running shoes for all terrains.'),
        ('T-Shirt', 'Clothing', 799.00, 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&h=500&fit=crop', 'Cotton t-shirt available in multiple colors.'),
        ('Blender', 'Home & Kitchen', 3499.00, 'https://images.unsplash.com/photo-1584622181563-430f63602d4b?w=500&h=500&fit=crop', 'Powerful blender for smoothies and more.'),
        ('Laptop Stand', 'Electronics', 1299.00, 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500&h=500&fit=crop', 'Adjustable stand for laptops.'),
        ('Watch', 'Accessories', 1999.00, 'https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=500&h=500&fit=crop', 'Stylish watch with leather strap.'),
        ('Sandals', 'Footwear', 599.00, 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&h=500&fit=crop', 'Comfortable sandals for summer.'),
        ('Jeans', 'Clothing', 1499.00, 'https://images.unsplash.com/photo-1542272604-787c62d465d1?w=500&h=500&fit=crop', 'Denim jeans in various sizes.'),
        ('Coffee Maker', 'Home & Kitchen', 2299.00, 'https://images.unsplash.com/photo-1517668808822-9ebb02ae2a0e?w=500&h=500&fit=crop', 'Automatic coffee maker for home use.'),
    ]
    cursor.executemany('INSERT INTO products (name, category, price, image_url, description) VALUES (?, ?, ?, ?, ?)', sample_products)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print('Database initialized with sample data.')