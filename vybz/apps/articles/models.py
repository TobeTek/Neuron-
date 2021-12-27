from django.db import models
from apps.songs.models import Genre
from django.contrib.auth import get_user_model


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=10)

class Article(models.Model):    
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    header_image = models.ImageField(upload_to="articles/header_imgs", null=True, blank=True)
    time_published = models.DateTimeField(auto_created=True)
    time_last_edited = models.DateTimeField(null=True, auto_now=True)

    # Url Routing
    slug  = models.SlugField(editable=False)

    tags = models.ManyToManyField(Tag, related_name="articles")
    

class Comment(models.Model):
    pass

class Like(models.Model):
    pass
