# RESTful-events-api

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON-web-tokens&logoColor=white)![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

This is a simple Django REST framework project with user authentication, event creation. It provides a basic CRUD operations.

## Features:

- User registration and JWT-based authentication.
- Event management with the ability to create, update, delete events.
- Filtering and search events.
- Email notifications for event registration.
- API documentation and testing implemented using Swagger for a clear and interactive interface.

## Requirements:

- Python
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL


## Using Docker:

Clone the repository:
   ```bash
   git clone https://github.com/barabarinov/RESTful-events-api.git
   ```

Run the following command to prepare your environment for the first run:
```shell
make prepare
```

Build and start the application using Docker:
```shell
make up
```

Open your browser and navigate to http://localhost:8000/:

Use the default credentials to log in:
- **Username:** admin
- **Password:** admin

If needed, you can update these credentials in the .env file before starting the containers.

To stop the running containers, use:
```shell
make down
```

To remove all containers, images, and volumes, use:
```shell
make clean
```

### Additional Notes:
- Make sure you have Docker installed and running before you start.
- The app will automatically create an admin user the first time you run it. If an admin already exists, it will skip this step and let you know.
- Static files are automatically collected during the Docker build process (python manage.py collectstatic). No additional actions are required.

### Email Notifications:

If you want to check email notification feature, follow these steps:

1. Sign up for a free account (or log in if you already have an account) on [SendGrid’s official website](https://sendgrid.com/en-us).
2. Generate a ***SendGrid API Key*** and paste into the .env file under ***SENDGRID_API_KEY***.
3. Configure ***Single Sender Verification*** in your SendGrid account, then paste the verified email into the .env file as ***FROM_EMAIL***.

## API Endpoints

### User Registration and Authentication:

🟢`POST /api/users/register/`: Register a new user.

🟢`POST /api/users/token/`: Get JWT access token.

🟢`POST /api/users/token/refresh/`: Refresh the JWT access token.

🟢`POST /api/users/token/verify/`: Verify the validity of a given JWT access token.

### Event Endpoints:

🟣`GET /api/events/`: List all events.

🟢`POST /api/events/`: Create a new event (requires authentication).

🟢`POST /api/events/<event_id>/register/`: Register an user for a specific event (requires authentication).

🟣`GET /api/events/<event_id>/`: Retrieve an single event.

🟠`PUT /api/events/<event_id>/`: Update an event's content (requires authentication).

🟡`PATCH /api/events/<event_id>/`: Partially update an event's content (requires authentication).

🔴`DELETE /api/events/<event_id>/`: Delete an event (requires authentication).

### Search and Filtering:

🟣`GET /api/events/?search=concert`: Search events by title or description.

🟣`GET /api/events/?location=Kyiv`: Filter events by location.

🟣`GET /api/events/?datetime=2024-12-16T07:17:51Z`: Filter events by datetime.

🟣`GET /api/events/?datetime_after=2024-12-16T00:00:00Z&datetime_before=2024-12-31T23:59:59Z`: Filter events by a datetime range.

🟣`GET /api/events/?organizer=1`: Filter events by organizer (using user ID).

🟣`GET /api/events/?ordering=datetime`: Order events by datetime in ascending order.

🟣`GET /api/events/?ordering=-title`: Order events by title in descending order.


### Testing

User Registration:
```shell
curl -X POST http://localhost:8000/api/users/register/ \
-H "Content-Type: application/json" \
-d '{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "securepassword123"
}'
```

Get JWT Access Token:
```shell
curl -X POST http://localhost:8000/api/users/token/ \
-H "Content-Type: application/json" \
-d '{
  "username": "admin",
  "password": "admin"
}'
```

Refresh JWT Token:
```shell
curl -X POST http://localhost:8000/api/users/token/refresh/ \
-H "Content-Type: application/json" \
-d '{
  "refresh": "your-refresh-token"
}'
```

Verify JWT Token:
```shell
curl -X POST http://localhost:8000/api/users/token/verify/ \
-H "Content-Type: application/json" \
-d '{
  "token": "your-access-token"
}'
```

List All Events:
```shell
curl -X GET http://localhost:8000/api/events/
```

Create a New Event (requires authentication):
```shell
curl -X POST http://localhost:8000/api/events/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your-access-token" \
-d '{
  "title": "RY X",
  "description": "RY X is currently touring across 13 countries and has 24 upcoming concerts.",
  "location": "Kyiv",
  "datetime": "2025-01-09T15:00:00Z"
}'
```

Retrieve a Specific Event:
```shell
curl -X GET http://localhost:8000/api/events/1/
```

Update an Event (requires authentication):
```shell
curl -X PUT http://localhost:8000/api/events/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your-access-token" \
-d '{
  "title": "Updated Event Title",
  "description": "Updated description.",
  "location": "Lviv",
  "datetime": "2025-01-12T18:00:00Z"
}'
```

Partially Update an Event (requires authentication):
```shell
curl -X PATCH http://localhost:8000/api/events/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your-access-token" \
-d '{
  "title": "Partially Updated Title"
}'
```

Delete an Event (requires authentication):
```shell
curl -X DELETE http://localhost:8000/api/events/1/ \
-H "Authorization: Bearer your-access-token"
```
