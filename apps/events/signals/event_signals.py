from django.contrib.auth.signals import (user_logged_in, user_logged_out,
                                          user_login_failed)
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.devices.models import Device

from ..models import Event

#-----------------------------------------------
# Device lifecycle -> Event log
#-----------------------------------------------

@receiver(post_save, sender=Device)
def log_device_saved(sender, instance, created, **kwargs):
    if created:
        Event.objects.create(
            event_type="Device Created",
            event_description=f"Device '{instance.device_name}' was created.",
            device=instance,
            severity=Event.SavertyChoices.INFO,
        )
    else:
        Event.objects.create(
            event_type="Device Updated",
            event_description=f"Device '{instance.device_name}' was updated.",
            device=instance,
            severity=Event.SavertyChoices.INFO,
        )


@receiver(post_delete, sender=Device)
def log_device_deleted(sender, instance, **kwargs):
    # instance's row is already gone from the DB by this point, so the
    # event can't keep a device FK -- it's recorded as a "System" event.
    Event.objects.create(
        event_type="Device Deleted",
        event_description=f"Device '{instance.device_name}' was deleted.",
        device=None,
        severity=Event.SavertyChoices.WARNING,
    )

#-----------------------------------------------
# User auth actions -> Event log
#-----------------------------------------------

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    Event.objects.create(
        event_type="User Login",
        event_description=f"User '{user.username}' logged in.",
        device=None,
        severity=Event.SavertyChoices.INFO,
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    if user is None:
        return
    Event.objects.create(
        event_type="User Logout",
        event_description=f"User '{user.username}' logged out.",
        device=None,
        severity=Event.SavertyChoices.INFO,
    )


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request=None, **kwargs):
    username = credentials.get("username", "unknown")
    Event.objects.create(
        event_type="Failed Login",
        event_description=f"Failed login attempt for username '{username}'.",
        device=None,
        severity=Event.SavertyChoices.WARNING,
    )
