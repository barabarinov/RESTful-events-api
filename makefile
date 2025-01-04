# Variables
ENV_FILE = .env
EXAMPLE_ENV_FILE = .env.example

# Default target
all: prepare up

# Check if .env exists, otherwise rename .env.example to .env
prepare:
	@if [ ! -f $(ENV_FILE) ]; then \
		echo "Renaming $(EXAMPLE_ENV_FILE) to $(ENV_FILE)..."; \
		mv $(EXAMPLE_ENV_FILE) $(ENV_FILE); \
	else \
		echo "$(ENV_FILE) already exists."; \
	fi

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
