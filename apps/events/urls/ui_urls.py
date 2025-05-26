from django.urls import path
from ..views import ui

app_name = "events"

urlpatterns = [
    path("", ui.test, name="events")
]
