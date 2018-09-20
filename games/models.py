from django.db import models
import uuid

# Create your models here.

class Player(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField('Name', max_length=20, help_text='player name')
	games_played_field = models.IntegerField(default=0)
	games_won_field = models.IntegerField(default=0)



	def games_played(self):
		game_player1 = Game.objects.filter(player1=self.id).count()
		game_player2 = Game.objects.filter(player2=self.id).count()

		gp_sum = game_player1 + game_player2

		self.games_played_field = gp_sum
		self.save()

		return game_player1 + game_player2

	def games_won(self):
		games_won = Game.objects.filter(winner=self.id).count()

		self.games_won_field = games_won
		self.save()

		return games_won

	



	def __str__(self):
		return self.name




class Game(models.Model):
	

	player1 = models.ForeignKey(Player, on_delete='PROTECT', related_name='player1')
	player2 = models.ForeignKey(Player, on_delete='PROTECT', related_name='player2')
	winner = models.ForeignKey(Player, on_delete="PROTECT", related_name='winner')


	


	def __str__(self):
		return self.player1.name + self.player2.name





#create a user and save to database










