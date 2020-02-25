from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    followers = models.ManyToManyField('self', default=None, related_name='follow', blank=True, symmetrical=False)

    def __str__(self):
        return self.username
