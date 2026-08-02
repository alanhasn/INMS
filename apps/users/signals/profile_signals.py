from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Profile

#-----------------------------------------------

# Signal to create or update user profile when User instance is created or updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created: # When a new User is created, create a corresponding Profile
        # first_name defaults to the username so Profile.clean()'s
        # "at least one of First/Last Name" rule doesn't fail on a fresh signup.
        Profile.objects.create(user=instance, first_name=instance.username)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance, first_name=instance.username)
