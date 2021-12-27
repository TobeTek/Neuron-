from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.songs import models as song_models 

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    REQUIRED_FIELDS = ["age"]

class Profile(models.Model):
    # Music preference genre etc.
    # Religion
    # Use Censor
    # fav_genres = models.ManyToManyField(Genre,null=True, blank=True)
    user = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE)
    use_censor = models.BooleanField(default=False)
    pass

    