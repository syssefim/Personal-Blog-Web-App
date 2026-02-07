# Personal Blog Web Application

A full-stack Content Management System (CMS) built with Python and Flask. This application allows an administrator to log in, write, edit, and delete articles, while visitors can browse and read content. Additionally, it uses a PostgreSQL database for storage.

## 🚀 Features
- **Public View:** Home page listing all articles (sorted by newest) and individual article pages.
- **Admin Dashboard:** Secure interface to manage content.
- **CRUD Operations:** Create, Read, Update, and Delete articles.
- **Authentication:** Session-based login system.
- **Database:** Persistent storage using PostgreSQL and SQLAlchemy ORM.

## 🛠️ Tech Stack
- **Backend:** Python 3, Flask
- **Database:** PostgreSQL, SQLAlchemy
- **Frontend:** HTML5, Jinja2 Templates
- **Driver:** Psycopg2-binary

## 📋 Prerequisites
Ensure you have the following installed on your machine:
- Python 3.x
- PostgreSQL (v12 or higher recommended)
- pip (Python package manager)

## ⚙️ Installation & Setup

### 1. Clone the Repo
    git clone https://github.com/syssefim/Personal-Blog-Web-App
### 2. Install Dependencies
    pip install flask flask-sqlalchemy psycopg2-binary
### 3. Database Setup
You need to create the database and user. Open your PostgreSQL tool (pgAdmin or psql) and run:

CREATE DATABASE personal_blog_db;
CREATE USER personal_blog_admin WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE personal_blog_db TO blog_admin;

### 4. Database Seeding
Now, populate the database with sample data by running the following command in the terminal:

    python3 seed_db.py

### 5. Configuration
Create a file named `.env` in the root directory to store sensitive credentials, and add the following lines:

    DB_PASSWORD=YOUR_PASSWORD_HERE
    DB_USER=postgres
    DB_NAME=personal_blog_db
    DB_HOST=localhost
    DB_PORT=5432
Set 'DB_PASSWORD' to be your PostgreSQL password.

### 6. Run the Application
In your terminal, run:
python app.py

### 7. Access the App
Open your web browser and go to:
http://127.0.0.1:5000/

