from django.db import models
from django.contrib.auth import get_user_model

class Song(models.Model):
    # Site user's can upload their own music to share and allow for contributions
    name = models.CharField(max_length=100)
    artiste = models.ForeignKey(get_user_model(),null=True, on_delete=models.DO_NOTHING, related_name="songs")
    featured_artistes = models.ManyToManyField(get_user_model(), blank=True, related_name="collabs")
    file = models.FileField(null=True, blank=True)

        
class Genre(models.Model):
    name = models.CharField(max_length=10)
    songs = models.ManyToManyField(Song, related_name="genre", blank=True)
    pass

