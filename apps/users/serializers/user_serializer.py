from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for User model that includes profile information.
        This serializer provides a read-only representation of the user,
        including username, email, date joined, last login, and profile details.
    """

    profile = serializers.SerializerMethodField("get_profile") 

    def get_profile(self, obj):
        return {
            "first_name": obj.profile.first_name if obj.profile.first_name else None,
            "last_name": obj.profile.last_name if obj.profile.last_name else None,
            "profile_image": obj.profile.profile_image.url if obj.profile.profile_image else None,
            "bio": obj.profile.bio if obj.profile else None,
            "phone_number": obj.profile.phone_number if obj.profile else None,
            "address": obj.profile.address if obj.profile else None,
            "created_at": obj.profile.created_at if obj.profile else None,
        }
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "date_joined",
            "last_login",
            "profile"
        ]
    
