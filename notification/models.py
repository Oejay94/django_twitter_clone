from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from twitteruser.models import CustomUser
from tweet.models import Tweet

class Notification(models.Model):
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
