from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings



class Device(models.Model):
    device_name = models.CharField(max_length=100 , verbose_name="Device Name")

    class DeviceTypeChoices(models.TextChoices):
        ROUTER = "Router"
        SWITCH = "Switch"
        FIREWALL = "Firewall"
        ACCESS_POINT = "Access Point"
        SERVER = "Server"
        OTHER = "Other"

    device_type = models.CharField(max_length=100 ,choices=DeviceTypeChoices.choices, verbose_name="Device Type")
    ip_address = models.GenericIPAddressField(verbose_name="IP Address")
    mac_address = models.CharField(max_length=17 , verbose_name="MAC Address")
    port = models.PositiveIntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        verbose_name="Port",
        help_text="Management/service port (1-65535), if applicable.",
    )
    location = models.CharField(max_length=100 , verbose_name="Location")
    description = models.TextField(blank=True , null=True , verbose_name="Description")
    class StatusChoices(models.TextChoices):
        ACTIVE = "Active"
        INACTIVE = "Inactive"
        MAINTENANCE = "Maintenance"
        ONLINE = "Online"
        OFFLINE = "Offline"
        WARNING = "Warning"

    status = models.CharField(max_length=20 ,choices=StatusChoices.choices, default=StatusChoices.ACTIVE , verbose_name="Status")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , verbose_name="Device Owner" , related_name="owned_devices")

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
        ordering = ['device_name'] # Order by device name 