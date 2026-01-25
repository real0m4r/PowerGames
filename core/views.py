from django.shortcuts import render

def home(request):
    context = {
        'title': 'Welcome to PowerGames',
        'message': 'Your Django application is running successfully!'
    }
    return render(request, 'core/home.html', context)