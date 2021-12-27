from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model

from . import models

@receiver(post_save, sender=models.Article)
def create_profile_handler(sender, instance, created, **kwargs):
    if created:
        return
    # Create a profile object only if an article is edited
    profile = models.Profile(user=instance)
    profile.save()

