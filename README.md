# BookNet-library

A web-based book library built with Django. Users can register, add books with covers and files, browse the catalog, download books, and maintain a profile with an avatar and bio.

## Features

- User registration and login
- User profiles (avatar, bio) and public profile pages
- Book catalog with genres, covers, and search
- Adding books with cover image and file upload (fb2, zip, etc.)
- Book file downloads
- Django admin panel for content management

## Tech Stack

- Python 3 / Django 6
- SQLite (default database)
- Pillow (image uploads)

## Project Structure

```
BookNet-library/
├── manage.py
├── requirements.txt
├── myproject/        # project settings (settings, urls)
├── books/            # app: books, genres, catalog
├── accounts/         # app: registration, profiles
├── static/           # static files (logo, banners)
└── media/            # uploaded files (covers, books, avatars)
```

## Setup and Running

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd BookNet-library
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\activate   # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your secret key:

   ```bash
   cp .env.example .env
   ```

   Then generate a secret key and put it into `.env`:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (for the admin panel):

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

The site will be available at: http://127.0.0.1:8000/

- Book catalog: `/`
- Admin panel: `/admin/`
- Login/register: `/accounts/login/`, `/accounts/register/`

## Notes

- The project is configured for development: `DEBUG = True`, static and media files are served by Django automatically.
- Uploaded files are stored in `media/` (covers — `media/book_covers/`, book files — `media/book_files/`, avatars — `media/avatars/`).
- For production you will need to set `ALLOWED_HOSTS`, `DEBUG = False`, configure a web server for static/media files, and move `SECRET_KEY` to environment variables.