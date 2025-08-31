from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Profile

#-----------------------------------------------

# Signal to create or update user profile when User instance is created or updated
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: # When a new User is created, create a corresponding Profile
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
