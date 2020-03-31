from django import forms

from .models import TwitterUser

class create_account(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())