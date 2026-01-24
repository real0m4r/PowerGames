#!/bin/bash

echo "Building application..."
python manage.py collectstatic --noinput
python manage.py migrate
