from django import forms

class PlayerForm(forms.Form):
	name = forms.CharField(label='player name', max_length=30)