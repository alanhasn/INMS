from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    device_name = models.CharField(max_length=100 , verbose_name="Device Name")
    device_type = models.CharField(max_length=100 , verbose_name="Device Type")
    ip_address = models.GenericIPAddressField(verbose_name="IP Address")
    mac_address = models.CharField(max_length=17 , verbose_name="MAC Address")
    location = models.CharField(max_length=100 , verbose_name="Location")

    class StatusChoices(models.TextChoices):
        ACTIVE = "Active"
        INACTIVE = "Inactive"

    status = models.CharField(max_length=20 ,choices=StatusChoices.choices, default=StatusChoices.ACTIVE , verbose_name="Status")
    owner = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="Device Owner" , related_name="owned_devices")

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"
        ordering = ['device_name'] # Order by device name 