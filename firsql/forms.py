from django import forms
from django.contrib.auth.models import User
from .models import Profile



class CardNumberForm(forms.ModelForm):
	card_number = forms.CharField(max_length=16, required=True)

	class Meta:
		model = Profile
		fields = ('card_number',)


class MoneyAmountForm(forms.ModelForm):
	money_amount = forms.IntegerField()

	class Meta:
		model = Profile
		fields = ('money_amount',)
