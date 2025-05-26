from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from ..serializers.profile_serializer import UserProfileSerializer
from ..serializers.user_serializer import UserSerializer
from ..models.profile import Profile

class UserProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.select_related("user")
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        qs =  super().get_queryset()
        return qs.filter(user=self.request.user)


class UserProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get_object(self):
        return self.request.user.profile

class UserInfoAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(id=self.request.user.id)
