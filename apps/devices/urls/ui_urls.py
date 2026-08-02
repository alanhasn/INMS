from django.urls import path

from ..views import ui

app_name = "devices"

urlpatterns = [
    path("" , ui.test , name="devices"),
    path("create/", ui.create_device, name="device_create"),
    path("<int:pk>/edit/", ui.update_device, name="device_update"),
    path("<int:pk>/delete/", ui.delete_device, name="device_delete"),
]