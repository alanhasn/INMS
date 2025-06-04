# ===========Importing Required Libraries and Modules=========================
from django.urls import path
import django.contrib.auth.views as auth
from ..views import ui
# ---------------------------------------------------------------------------

urlpatterns = [
     # UI URLs for User Management
    path("profile/", ui.ProfilePage, name="profile"),
    path("edit-profile/", ui.EditProfile, name="edit_profile"),
    path("register/", ui.Register, name="register"),
    path("login/", ui.LoginPage, name="login"),
    path("logout/", ui.LogoutPage, name="logout"),
    path("dashboard/", ui.DashboardPage, name="dashboard"),

     #================================================================
     # Password Reset URLs
     #================================================================
     # This URL is used to display the password reset form
     # It uses the CustomPasswordResetView for save the email in session
     # and send the password reset email to the user.
     path("password-reset/",
          ui.CustomPasswordResetView.as_view(template_name="users/password_reset.html"),
          name="password_reset"),
    path("password-reset-done/",
         auth.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         auth.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         auth.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),

     # This URL is used to resend the password reset email
     path("resend-reset-email/", ui.resend_password_reset_email, name="resend_reset_email"),

]
