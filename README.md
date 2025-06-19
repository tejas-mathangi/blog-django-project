# Blog Django Project

This is a simple blog application built with Django. The application allows users to create, read, update, and delete blog posts (CRUD functionality). The project demonstrates how little code is required in Django to achieve these core features.

In a small amount of code I've built a blog application that allows for creating, reading, updating, and deleting blog posts. This core functionality is known by the acronym CRUD: Create-Read-Update-Delete. While there are multiple ways to achieve this same functionality–I have used function-based views and also written my own class-based views– Very little code in Django to make this happen.

## Features

- Create new blog posts
- Read/view existing blog posts
- Update blog posts
- Delete blog posts

## Getting Started

### Prerequisites

- Python 3.x
- Django (see `requirements.txt`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tejas-mathangi/blog-django-project.git
   cd blog-django-project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**  
   Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
blog-django-project/
├── blog/                 # Django app with models, views, templates
├── blog_django_project/  # Project settings and configuration
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
```

## License

This project is licensed under the MIT License.
