from django import forms

from twitteruser.models import TwitterUser

class login_form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())