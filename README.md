# Article Django

A Django-based web application for managing articles.

## Features

- User registration and authentication
- Create, read, update, and delete articles
- Search functionality
- Article categorization by subject
- Admin panel for content management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JoHN-MTHW/Aricle-django.git
   cd Aricle-django
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to view the application.

## Usage

- Register a new account or log in
- Create articles from the dashboard
- Browse articles by subject
- Use the search feature to find specific content

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
