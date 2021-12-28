from django.db import models
from vybz.apps.songs.models import Genre
from django.contrib.auth import get_user_model

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now=True)

class Article(models.Model):    
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="authors_articles")
    
    published = models.BooleanField(default=False)
    header_image = models.ImageField(upload_to="articles/header_imgs", null=True, blank=True)
    
    time_published = models.DateTimeField(auto_now_add=True, blank=True)
    time_last_edited = models.DateTimeField(null=True, auto_now=True, blank=True)

    slug  = models.SlugField(editable=False, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="articles")
    likes = models.ManyToManyField(get_user_model(), blank=True, related_name="my_likes")
    dislikes = models.ManyToManyField(get_user_model(), blank=True, related_name="my_dislikes")

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    children = models.ManyToManyField("Comment", blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    body = models.CharField(max_length=255)

    time_published = models.DateTimeField(auto_created=True)
    
