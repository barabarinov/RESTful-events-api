# RESTful-events-api

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON-web-tokens&logoColor=white)![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

This is a simple Django REST framework project with user authentication, event creation. It provides a basic CRUD operations.

## Features

- **User registration** and JWT-based authentication.
- **Event management** with the ability to create, update, delete events.

## Requirements

- Python 3.11.0
- Django 5.1.4
- Django REST Framework
- Simple JWT
- PostgreSQL

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/barabarinov/RESTful-events-api.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
4. Set up environment variables:

   Create a `.env` file in the project root and add your values:

   ```bash
   SECRET_KEY=<your-secret-key>
   DB_NAME=<your-db-name>
   DB_USER=<your-db-user>
   DB_PASSWORD=<your-db-password>
   DB_HOST=<your-db-host>
   DB_PORT=<your-db-port>
   ```
   
5. Run migrations to set up the database:

   ```bash
   python manage.py makemigrations
   ```
   
   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```
   
7. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Using Docker
Run `docker-compose` command to build and up containers:
```shell
docker-compose up --build
```
Make migrations:
```shell
docker-compose exec web python manage.py migrate
```
Create superuser:
```shell
docker-compose exec web python manage.py createsuperuser
```

## API Endpoints

### User Registration and Authentication

- `POST /api/users/register/`: Register a new user.
- `POST /api/users/token/`: Get JWT access token.
- `POST /api/users/token/refresh/`: Refresh the JWT access token.
- `POST /api/users/token/verify/`: Verify the validity of a given JWT access token.

### Event Endpoints

- `GET /api/events/`: List all events.
- `POST /api/events/`: Create a new event (requires authentication).
- `POST /api/events/<event_id>/register/`: Register a user for a specific event (requires authentication).
- `GET /api/events/<event_id>/`: Retrieve a single event.
- `PUT /api/events/<event_id>/`: Update a event's content (requires authentication).
- `PATCH /api/events/<event_id>/`: Partially update a event's content (requires authentication).
- `DELETE /api/events/<event_id>/`: Delete a event (requires authentication).
