from django.db import models
from django.utils import timezone

from twitteruser.models import TwitterUser

class Tweet(models.Model):
    body = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "By {} on {}".format(self.created_by, self.created_on)