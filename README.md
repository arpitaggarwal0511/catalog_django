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


## 🌐 Live Demo
[live](https://catalog-django-3.onrender.com/)  

---

## 📁 Project Structure

```
catalog_back/        → Main Django project (settings, URLs)
products/            → App that handles product logic
templates/           → HTML templates
startup.sh           → Deployment script
requirements.txt     → Project dependencies
manage.py            → Django command utility
```

---

## 🚀 Installation (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/arpitaggarwal0511/catalog_django.git
cd catalog_django
```

### 2. Create and activate virtual environment  
**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```

Open in browser:
```
http://127.0.0.1:8000/products/
```

---

## 🛠 Deployment (Render)

This project uses a `startup.sh` script which:

- Runs migrations  
- Collects static files  
- Creates superuser automatically (optional)  
- Starts Gunicorn  

### Render **Start Command**
```bash
bash startup.sh
```

### Render **Build Command**
```bash
pip install -r requirements.txt
```

### Required Environment Variables (optional)
To auto-create admin user on first deploy:

```
DJANGO_SU_USERNAME=admin
DJANGO_SU_PASSWORD=yourpassword
DJANGO_SU_EMAIL=optional@example.com
```

---

## 📡 JSON API Example

Example endpoint:

```
GET /products/3/json/
```

Example response:
```json
{
  "id": 3,
  "name": "Sample Product",
  "price": "999.00",
  "rating": 4.7,
  "size": "M",
  "description": "Simple product description",
  "image_url": "https://example.com/image.jpg"
}
```

This JSON is used by the “Details” popup on the product listing page.

---


## 📘 Why This Project Exists

This project was created as part of an internship assignment to learn:

- Django backend basics  
- Project structure and app creation  
- Rendering HTML with templates  
- CRUD model understanding  
- Filtering, searching, modal display  
- Deployment workflow  

The goal is to keep the project **simple, readable, and easy to explain in a viva**.

---

## 📄 License
This project is for educational/demo purposes.  
You may use and modify it freely.


