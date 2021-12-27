from django.db import models
from apps.songs.models import Genre
from django.contrib.auth import get_user_model


# Create your models here.
class Article(models.Model):    
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
class Tag(models.Model):
    pass

class Comment(models.Model):
    pass

class Like(models.Model):
    pass
