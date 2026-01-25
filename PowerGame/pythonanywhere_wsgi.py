# This file is used by PythonAnywhere to run your Django application
# Place this file at: /var/www/yourusername_pythonanywhere_com_wsgi.py on PythonAnywhere

import os
import sys
from pathlib import Path

# Add your project to the path
project_home = '/home/yourusername/PowerGame'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set up Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'PowerGame.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
