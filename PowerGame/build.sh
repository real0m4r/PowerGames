#!/bin/bash

echo "Building application..."
python manage.py collectstatic --noinput --clear
echo "Build completed successfully!"
