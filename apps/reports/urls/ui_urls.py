from django.urls import path
from ..views import ui

app_name = "reports"

urlpatterns = [
    path("" , ui.test)
]