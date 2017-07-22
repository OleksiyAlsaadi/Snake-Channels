import json

from django import forms

#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth.models import User
success = 0;

class SuggestionForm(forms.Form):
    global success
    suggestion = forms.CharField(
        label='',
        max_length=140,
        widget=forms.TextInput(attrs={
            'placeholder': 'Load Game'
            }))
