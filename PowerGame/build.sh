#!/bin/bash

set -e

echo "Building Django application for Netlify..."
python manage.py collectstatic --noinput --clear
echo "Build completed successfully!"
