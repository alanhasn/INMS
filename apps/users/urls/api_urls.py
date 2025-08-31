from django.urls import path
# from ..views.api import (
#     UserProfileListAPIView,
#     UserProfileUpdateAPIView,
#     UserInfoAPIView,
# )
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

# This file contains API URLs for user management, including JWT authentication and user profile handling.
# Not all URLs are currently implemented, but the structure is set up for future development.
#-------------------------------------------------------------------------------------------------------------------------------

app_name = "users_api"

urlpatterns = [
#     # JWT authentication URLs
#     path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
#     path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),




#     path('user-profile/', UserProfileListAPIView.as_view(), name='user-profile-list'),
#     path('user-profile/update/', UserProfileUpdateAPIView.as_view(), name='user-profile-update'),
#     path('me/', UserInfoAPIView.as_view(), name='me'),
]