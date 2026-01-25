#!/bin/bash

set -e

echo "Building Django application for PythonAnywhere..."
python manage.py collectstatic --noinput --clear
echo "Running migrations..."
python manage.py migrate --noinput
echo "Build completed successfully!"
