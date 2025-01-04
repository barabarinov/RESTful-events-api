# Variables
ENV_FILE = .env
EXAMPLE_ENV_FILE = .env.example

# Default target
all: prepare up

# Prepare first-time initialization of the application TODO: Create sh script for this command
prepare:
	chmod +x prepare_env.sh
	./prepare_env.sh

# Build and start the Docker containers
up:
	docker-compose up --build

# Stop the Docker containers
down:
	docker-compose down

# Clean up Docker containers, volumes, and images
clean:
	docker-compose down -v --rmi all
	rm -f $(ENV_FILE)
