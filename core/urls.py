from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('games', views.all_games, name='all_games'),
    path('games/<int:game_id>/', views.game, name='game'),
    path('home', views.home, name='home'),

    path('search', views.search, name='search'),
]
