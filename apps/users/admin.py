from django.contrib import admin

from .models import Profile


@admin.register(Profile) # Register the Profile model with the admin site
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for the Profile model.
    """
    list_display = ("user__username","first_name","last_name","profile_image","created_at")
    search_fields = ("user__username","first_name","last_name")
    list_filter = ("user__username" , "country" , "city" ,  "phone_number")
    ordering = ("-created_at",)
    list_per_page = 20 # Number of records per page in the admin list view
    list_display_links = ("user__username", "first_name", "last_name")
    