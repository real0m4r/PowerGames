import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PowerGame.settings')

application = get_wsgi_application()

def handler(request):
    """Handle incoming HTTP requests"""
    return application(request.environ, request.start_response)
