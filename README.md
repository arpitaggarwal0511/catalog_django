# Product Catalog (Django Demo)

This is a small Django project built to demonstrate the basics of:

- Creating a Django backend  
- Working with models and migrations  
- Displaying products on a page  
- Searching and filtering  
- Returning JSON responses  
- Rendering templates  
- Deploying a Django app on Render  

It is not a full e-commerce website.  
The goal is to showcase backend understanding in a simple and clean way.

---

## Features

### ✅ Product List Page
- Shows all products from the database  
- Displays name, price, rating, size and image  
- Presented in simple card layout  

### ✅ Search
- Search products by name or description  

### ✅ Filters
- Filter by:
  - Size  
  - Min/Max Price  
  - Min Rating  

### ✅ Product Detail Popup
- A “Details” button fetches product info from a JSON endpoint  
- Data is shown inside a modal popup  

### ✅ Admin Panel
- Django admin is used to create and manage products  
- Admin login can be created from environment variables in deployment  

---

## Project Structure
/catalog_back → Main Django project (settings, URLs, wsgi)
/products → App that handles product logic
/templates → HTML templates
startup.sh → Deployment script (migrations, static files, superuser)
requirements.txt → Python dependencies
manage.py → Django command-line utility
