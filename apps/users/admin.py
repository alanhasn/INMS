from django.contrib import admin
from .models import CustomUser
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

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin interface for the CustomUser model.
    """
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff", "is_active")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("role", "is_staff", "is_active")
    ordering = ("-date_joined",)
    list_per_page = 20 # Number of records per page in the admin list view
    list_display_links = ("username", "email")