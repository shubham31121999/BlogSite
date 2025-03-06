# BlogSite  
A social media-like blog platform built using Django, allowing users to create, read, update, and delete blog posts with authentication features.

---

## Features
- ✅ User Authentication (Registration, Login, Logout)  
- ✅ Blog Post Management (CRUD operations)  
- ✅ User Profiles with bio and profile pictures  
- ✅ Comments & Likes on posts  
- ✅ Django Admin Panel for content management  

---

## Project Requirements

### 1. User Authentication
- Implement user registration, login, and logout functionality using Django's built-in authentication system.

### 2. Blog Post Model
Create a `Post` model with the following fields:
- `title`: CharField  
- `content`: TextField  
- `author`: ForeignKey to User  
- `created_at`: DateTimeField (`auto_now_add=True`)  
- `updated_at`: DateTimeField (`auto_now=True`)  
- `status`: ChoiceField (`Draft`, `Published`)  

### 3. Views and Templates
Create views and templates for:
- Listing all blog posts  
- Creating a new blog post  
- Updating an existing blog post  
- Deleting a blog post  
- Viewing a single blog post  

### 4. Comment Model
Create a `Comment` model with:
- `post`: ForeignKey to Post  
- `author`: ForeignKey to User  
- `content`: TextField  
- `created_at`: DateTimeField (`auto_now_add=True`)  

### 5. Views and Templates for Comments
- Allow users to add comments to a blog post  
- Display comments under each blog post  

### 6. Like Functionality
- Implement a like button for each blog post  
- Track the number of likes for each post  

**Login Page Reference:**  
👉 [Login Page Template](https://codepen.io/technext/pen/PoprgzP)

---

## Installation Guide

### Prerequisites
Ensure you have the following installed:
- Python 3.x  
- `pip` (Python package manager)  
- Virtual environment tool (optional but recommended)  

### Steps to Install & Run

#### 1. Clone the Repository
```sh
git clone https://github.com/shubham31121999/BlogSite.git
cd BlogSite
```

#### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

#### 4. Run Migrations
```sh
python manage.py migrate
```

#### 5. Create a Superuser (for Admin Panel Access)
```sh
python manage.py createsuperuser
```

#### 6. Run the Development Server
```sh
python manage.py runserver
```

#### 7. Access the Site
- 🌐 **Frontend:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- 🔧 **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

---

## Project Setup & Development Workflow

1. **Create a Virtual Environment:**  
   ```sh
   python -m venv venv
   ```
2. **Activate the Virtual Environment:**  
   ```sh
   venv\Scripts\activate
   ```
3. **Create a Django Project Directory:**  
   ```sh
   django-admin startproject Blog
   ```
4. **Navigate to the Project Directory:**  
   ```sh
   cd Blog
   ```
5. **Create a Web App for the Project:**  
   ```sh
   python manage.py startapp socialsite
   ```
6. **Rename `Blog` Directory to `config` & Add Django for Settings Management.**  
7. **Restructure Files for Better Development Setup:**  
   - The `config` directory contains development settings (`base`, `local`, `production`).  
   - Test cases are placed in `tests.py`.  
8. **Modify `wsgi.py`, `asgi.py`, and `manage.py` to Reflect New Project Naming.**  
9. **Design and Implement the Login & Signup Page with a Slider Effect.**  
10. **User Signup Fields Include:**  
    - `First Name`, `Last Name`, `Password`, `Date of Birth`, `Email`.  
    - Each user is assigned a **unique ID** using `uuid`.  

---

## Technologies Used
- **Backend:** Django  
- **Database:** SQLite (default), can be configured for PostgreSQL  
- **Frontend:** Django Templates, HTML, CSS, JavaScript  

---

## License
This project is licensed under the **MIT License**.

---

## Contributing
Feel free to **fork** the repository and contribute!  
Submit a **pull request** with improvements or bug fixes.  

🚀 **Happy Coding!** 🚀
