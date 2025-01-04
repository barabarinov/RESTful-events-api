#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h db -p 5432; do
	sleep 1
done
echo "PostgreSQL is ready."

echo "Running migrations..."
python manage.py migrate
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
	echo "Creating superuser..."
	python manage.py createsuperuser --noinput \
		--username $DJANGO_SUPERUSER_USERNAME \
		--email $DJANGO_SUPERUSER_EMAIL || echo "Superuser already exists."
fi

$@

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec "$@"
