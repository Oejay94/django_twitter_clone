from django import forms

from .models import Tweet

class post_tweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'body'
        ]