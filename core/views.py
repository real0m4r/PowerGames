from django.shortcuts import render,  HttpResponseRedirect
from .models import Game
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)
        message = "login successful"

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("core:home") + "?message=" + message)
        else:
            return render(request, "core/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'core/login.html')


@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def all_games(request):
    games = Game.objects.all()
    paginator = Paginator(games, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/all_games.html', {'games': page_obj.object_list, 'page_obj': page_obj})
@login_required
def game(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'core/game.html', {'game': game})

@login_required
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        all_games = Game.objects.filter(iframe__contains=searched)
        return render(request, 'core/search.html', {'searched':searched,
                                                    'all_games':all_games})
    else:
        return render(request, 'core/search.html')