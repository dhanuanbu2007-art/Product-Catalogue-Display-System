# Dispro Store - Product Catalogue Website

A modern full-stack product catalogue website built with Flask (Python) backend and HTML/CSS/JavaScript frontend.

## Features

- Clean, professional e-commerce UI
- Category-wise product filtering
- Responsive design
- Cart functionality (basic count)
- SQLite database for products

## Setup

1. Ensure Python 3.13 is installed.
2. Install Flask: `pip install flask`
3. Run `python init_db.py` to initialize the database with sample data.
4. Run `python app.py` to start the server.
5. Open http://127.0.0.1:5000/ in your browser.

## Project Structure

- `app.py`: Flask backend with API endpoints
- `init_db.py`: Database initialization script
- `templates/index.html`: Main HTML template
- `static/css/style.css`: Stylesheet
- `static/js/script.js`: Frontend JavaScript
- `database.db`: SQLite database

## API Endpoints

- `GET /api/products?category=<category>`: Get products (filtered by category)
- `POST /api/add-product`: Add a new product (JSON payload)

## Technologies Used

- Backend: Python Flask
- Database: SQLite
- Frontend: HTML5, CSS3, JavaScript (ES6)