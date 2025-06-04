from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from ..models import Profile
# -----------------------------------------------------------------------------

# Signals to create and save Profile when a User is created or updated
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a Profile for every new User"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Save the profile whenever the user is saved"""
    instance.profile.save()
