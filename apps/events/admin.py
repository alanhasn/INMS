from django.contrib import admin

from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'event_date', 'device')
    search_fields = ('event_type' , "device__device_name")
    list_filter = ('event_type', 'device',)
    ordering = ('-event_date',)
    list_per_page = 20
    list_editable = ('device',)
