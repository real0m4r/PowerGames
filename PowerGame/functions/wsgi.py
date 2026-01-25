import os
import sys
import django
from pathlib import Path

# Setup Django
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PowerGame.settings')
django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

def handler(event, context):
    """Netlify Functions handler for WSGI"""
    # Convert Netlify event to WSGI environ
    http_method = event.get('httpMethod', 'GET')
    path = event.get('path', '/')
    headers = event.get('headers', {})
    body = event.get('body', '')
    
    environ = {
        'REQUEST_METHOD': http_method,
        'SCRIPT_NAME': '',
        'PATH_INFO': path,
        'QUERY_STRING': event.get('queryStringParameters', ''),
        'CONTENT_TYPE': headers.get('content-type', ''),
        'CONTENT_LENGTH': len(body) if body else 0,
        'SERVER_NAME': headers.get('host', 'localhost').split(':')[0],
        'SERVER_PORT': '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': None,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': True,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # Add headers to environ
    for header, value in headers.items():
        header_key = 'HTTP_' + header.upper().replace('-', '_')
        environ[header_key] = value
    
    # Store response info
    response = {'status': None, 'headers': {}}
    
    def start_response(status, response_headers):
        response['status'] = int(status.split()[0])
        response['headers'] = dict(response_headers)
    
    # Call WSGI app
    try:
        result = app(environ, start_response)
        body_content = b''.join(result)
        
        return {
            'statusCode': response['status'],
            'headers': response['headers'],
            'body': body_content.decode('utf-8') if isinstance(body_content, bytes) else body_content
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Internal Server Error: {str(e)}'
        }
