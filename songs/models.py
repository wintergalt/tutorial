import datetime
from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class Song(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

