from django.contrib import admin
from .models import Device
# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'device_type', 'ip_address', 'mac_address', 'location', 'status', 'owner')
    search_fields = ('device_name',"device_type")
    list_filter = ('status', 'device_type', 'location' , 'owner')
    ordering = ('device_name',)
    list_per_page = 20 # Number of records per page in the admin list view
    list_editable = ('status',) # Make status field editable in the list view
