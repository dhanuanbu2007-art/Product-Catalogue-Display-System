# 🛒 Product Catalogue Display System

## 📌 Project Description
The Product Catalogue Display System is a web-based application that allows users to view products in an organized and structured manner. Products are displayed category-wise, improving user experience and navigation.

The system also includes an admin panel to add new products and an "Add to Cart" feature to simulate an online shopping experience.

---

## 🎯 Features
- 📂 Category-wise product display  
- 🔍 Search and filter functionality  
- ➕ Add new products (Admin Panel)  
- 🛍️ Add to Cart feature  
- 🖼️ Product images display  
- 📱 Responsive and user-friendly UI  

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](screenshots/home.png)

### 🛒 Product Display
![Product Display](screenshots/products.png)

### ➕ Admin Panel (Add Product)
![Admin Panel](screenshots/admin.png)

### 🗂️ Category-wise View
![Category View](screenshots/category.png)

---

## 🧰 Technologies Used

### Frontend:
- HTML  
- CSS  
- JavaScript  

### Backend:
- Python (Flask)  

### Database:
- SQLite  

---

## 🗂️ Project Structure
project-folder/
│
├── app.py
├── database.db
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── script.js
│
└── screenshots/
├── home.png
├── products.png
├── admin.png
└── category.png


---

## ⚙️ Installation & Setup

### Step 1: Download or Clone Project
```bash
git clone <your-repo-link>
Step 2: Install Dependencies
pip install flask flask-cors
Step 3: Run Application
python app.py
Step 4: Open in Browser
http://127.0.0.1:5000/
🗃️ Database
SQLite database (database.db) is used
Table: products
Product Table Fields:
id
name
category
price
image_url
description
