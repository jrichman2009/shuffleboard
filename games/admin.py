from django.contrib import admin
from games.models import Game, Player

# Register your models here.
admin.site.register(Player)
admin.site.register(Game)