#!/bin/bash

# Check if .env file exists
if [ -f .env ]; then
  # Read and export variables from .env file
  export $(cat .env | xargs)
fi

# Clean package directories only if they exist
[ -d dist ] && rm -rf dist

# Remove all .egg-info directories if they exist
find . -name "*.egg-info" -type d -exec rm -rf {} +

# Publish package using Twine
poetry publish --username $PYPI_USERNAME --password $PYPI_PASSWORD --build
