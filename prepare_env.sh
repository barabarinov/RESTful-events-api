#!/bin/bash

ENV_FILE=".env"
EXAMPLE_ENV_FILE=".env.example"

if [ ! -f "$ENV_FILE" ]; then
	echo "Renaming $EXAMPLE_ENV_FILE to $ENV_FILE..."
	mv "$EXAMPLE_ENV_FILE" "$ENV_FILE"
else
	echo "$ENV_FILE already exists."
fi
