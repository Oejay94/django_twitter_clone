from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class create_account(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'email',
            'age'
        ]
    
    def __init__(self, *args, **kwargs):
        super(create_account, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None