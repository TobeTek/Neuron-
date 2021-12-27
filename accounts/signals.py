from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model

from . import models

@receiver(post_save, sender=get_user_model())
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create a profile object only if a user is newly created
    profile = models.Profile(user=instance)
    profile.save()

