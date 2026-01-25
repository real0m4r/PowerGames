from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """Home page view"""
    context = {
        'title': 'Welcome to Django on Vercel',
        'message': 'Your Django application is successfully running on Vercel!'
    }
    return render(request, 'home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Us',
        'message': 'This is a Django application deployed on Vercel'
    }
    return render(request, 'about.html', context)

def api_hello(request):
    """Sample API endpoint"""
    return JsonResponse({
        'message': 'Hello from Django API!',
        'status': 'success'
    })
