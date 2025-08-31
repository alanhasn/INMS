from django.contrib.auth.models import User
from rest_framework import serializers

from ..models.profile import Profile
from ..serializers.user_serializer import UserSerializer

# class UserProfileSerializer(serializers.ModelSerializer):
#     """
#     Serializer for User Profile model that includes user information.
#     This serializer provides a read-only representation of the user profile,
#     including user details, profile image, first name, last name, bio,
#     phone number, address, and creation date.
#     """
#     username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Profile
#         fields = [
#             "username",
#             "profile_image",
#             "first_name",
#             "last_name",
#             "bio",
#             "phone_number",
#             "city",
#             "country",
#             "created_at",
#         ]
