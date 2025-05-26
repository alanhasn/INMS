from django.db import models
from apps.devices.models import Device

class Event(models.Model):
    event_type = models.CharField(max_length=100, verbose_name="Event Type")
    event_description = models.TextField(verbose_name="Event Description")
    event_date = models.DateTimeField(auto_now_add=True, verbose_name="Event Date")
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Device")

    class SavertyChoices(models.TextChoices):
        INFO = "Info"
        WARNING = "Warning"
        ERROR = "Error"
        CRITICAL = "Critical" 

    severity = models.CharField(max_length=10, choices=SavertyChoices.choices, default=SavertyChoices.INFO, verbose_name="Severity")

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-event_date']
