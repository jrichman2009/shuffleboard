from django.contrib import admin
from django.urls import path
from games import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players', views.players, name='players'),
    path('games', views.games, name='games'),
    path('games/register', views.register, name='register'),
    path('players/new_player', views.new_player, name='new_player')
]