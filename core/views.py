from django.shortcuts import render
from .models import Game
from django.core.paginator import Paginator


def home(request):
    return render(request, 'core/home.html')
def game(request):
    games = Game.objects.all()
    paginator = Paginator(games, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/game.html', {'games': page_obj.object_list, 'page_obj': page_obj})
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        all_games = Game.objects.filter(iframe__contains=searched)
        return render(request, 'core/search.html', {'searched':searched,
                                                    'all_games':all_games})
    else:
        return render(request, 'core/search.html')