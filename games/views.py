from django.shortcuts import render
from games.models import Player, Game
from games.forms import PlayerForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	return render(request, 'index.html')


def players(request):
	player_list = Player.objects.all()

	context = {

	'player_list': player_list

	}
			
	return render(request, 'players.html', context=context)

def new_player(request):
	if request.method == "POST":
		new_player_form = PlayerForm(request.POST)
		if new_player_form.is_valid():
			user = Player()
			user.name = new_player_form.cleaned_data.get('name')
			user.save()

			return HttpResponseRedirect('/games/')
	else:
		form = PlayerForm

	context = {
	'form': PlayerForm
	}

	return render(request, 'new_player.html', context=context)



def games(request):
	return 

def register(request):
	return