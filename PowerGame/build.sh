#!/bin/bash

set -e

echo "Building application..."
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Only run migrations if not on Vercel (using file-based DB)
if [ -z "$VERCEL" ]; then
  echo "Running migrations..."
  python manage.py migrate --noinput
else
  echo "Skipping migrations on Vercel (using in-memory database)"
fi

echo "Build completed successfully!"
