# RESTful-events-api

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON-web-tokens&logoColor=white)![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

This is a simple Django REST framework project with user authentication, event creation. It provides a basic CRUD operations.

## Features

- **User registration** and JWT-based authentication.
- **Event management** with the ability to create, update, delete events.
- **Event management** with the ability to filtering and search events.

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
   
4. Create your local Postgres database. Next, create a user and grant all necessary permissions. Rename the `.env.example` file to `.env` and replace the constant values with your own. Leave DB_HOST=localhost unchanged for local running.

   ```bash
   SECRET_KEY=<your-secret-key>
   DB_NAME=<your-db-name>
   DB_USER=<your-db-user>
   DB_PASSWORD=<your-db-password>
   DB_HOST=localhost
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
Change DB_HOST in `.env` file to following value:

   ```bash
   ...
   DB_HOST=db
   ...
   ```

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
- `POST /api/events/<event_id>/register/`: Register an user for a specific event (requires authentication).
- `GET /api/events/<event_id>/`: Retrieve an single event.
- `PUT /api/events/<event_id>/`: Update an event's content (requires authentication).
- `PATCH /api/events/<event_id>/`: Partially update an event's content (requires authentication).
- `DELETE /api/events/<event_id>/`: Delete an event (requires authentication).

### Search and Filtering

- `GET /api/events/?search=concert`: Search events by title or description.
- `GET /api/events/?location=Kyiv`: Filter events by location.
- `GET /api/events/?datetime=2024-12-16T07:17:51Z`: Filter events by datetime.
- `GET /api/events/?datetime_after=2024-12-16T00:00:00Z&datetime_before=2024-12-31T23:59:59Z`: Filter events by a datetime range.
- `GET /api/events/?organizer=1`: Filter events by organizer (using user ID).
- `GET /api/events/?ordering=datetime`: Order events by datetime in ascending order.
- `GET /api/events/?ordering=-title`: Order events by title in descending order.
