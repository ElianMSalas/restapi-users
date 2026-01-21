# Django REST Users API

API REST para gestión de usuarios con autenticación JWT.

## Stack
- Python
- Django
- Django Rest Framework
- JWT Authentication

## Endpoints
- POST /api/users/register/
- POST /api/users/login/
- GET /api/users/profile/
- POST /api/users/token/refresh/

## Setup
```bash
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
