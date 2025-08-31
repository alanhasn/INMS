from django.urls import path

from ..views import ui

app_name = "devices"

urlpatterns = [
    path("" , ui.test , name="devices"),
]