from django.shortcuts import render
from .models import Game
from django.core.paginator import Paginator

def home(request):
    games = Game.objects.all()
    paginator = Paginator(games, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/home.html', {'games': games, 'page_obj': page_obj})