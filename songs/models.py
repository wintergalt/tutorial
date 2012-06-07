from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTime(auto_now_add=True)

class Song(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTime(auto_now_add=True)



