# ===================Imports===================
from datetime import timedelta

from django.contrib import messages  # Message framework
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, render
from django.utils import timezone

from apps.devices.models import Device
from apps.events.models import Event

from ..forms import (AuthenticationUserForm, CreateUserForm,  # My Custom Form
                     EditProfileForm)
from ..models import Profile  # My Custom Model


# ======== Main index view just redirect the User ========
def index_redirect(request):
    if request.user.is_authenticated:
        message = "Redirecting to your INMS Dashboard..."
        redirect_url = 'dashboard' 
    else:
        message = "Redirecting to Login page..."
        redirect_url = 'login'
    context = {'message': message, 'redirect_url': redirect_url}
    return render(request, "users/redirecting.html", context)


#==========Register View============
def Register(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect("profile") 

    if request.method == "POST":
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save() # save data to the database
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.") 
    else:
        form = CreateUserForm() # if its not valid form return empty form
    # Context Data    
    context = {
        "form":form
    }
    return render(request, "users/register.html", context=context)

# ==========login page==========
def LoginPage(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect("profile")
    
    if request.method == "POST":
        form = AuthenticationUserForm(data = request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get("username") # get username 
            password = form.cleaned_data.get("password") # get password

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("edit_profile")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")  
    else:
        form = AuthenticationUserForm()
    # Context Data    
    context = {
        "form":form
    }
    return render(request, "users/login.html", context=context)

# ============logout============
@login_required(login_url="login")
def LogoutPage(request):
    logout(request) # Clear the session
    return redirect("login")

# ============Password Reset=============
class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        # Save the email in the session
        email = form.cleaned_data.get('email') 
        if email:
            # Store the email in the session
            self.request.session['reset_email'] = email
        else:
            # If no email is provided, clear the session variable
            self.request.session.pop('reset_email', None)

        return super().form_valid(form) 
    
# ============Password Reset resend link=============
def resend_password_reset_email(request):
    if request.method == "POST":
        email = request.session.get("reset_email") # get the email from the session
        if email:
            try:
                form = PasswordResetForm({"email": email}) # create a form instance with the email
                if form.is_valid():
                    # Send the password reset email
                    form.save(
                        request=request, 
                        use_https=request.is_secure(), # Use HTTPS if the request is secure
                        email_template_name="registration/password_reset_email.html",
                    )
                    messages.success(request, "Password reset email sent.")
                else:
                    messages.error(request, "Invalid email address.")
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
        else:
            messages.error(request, "No email address found in session.")
    return redirect("password_reset_done") 

# ===============User Profile page===============
@login_required(login_url="login")
def ProfilePage(request):
    # get_or_create returns a tuple (object, created)
    # defaults= avoids ValidationError from Profile.clean(), which requires
    # at least one of first_name/last_name to be set.
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={"first_name": request.user.username},
    ) # Get the user profile

    if created:
        messages.info(request, "Profile created successfully. Please edit your profile to add more information.")

    # Context Data
    context = {
        "profile": profile # -> User Profile Info
    }
    return render(request, "users/profile.html", context)


# ============Edit Profile============
@login_required(login_url="login")
def EditProfile(request):
    """
    Display and process the EditProfileForm for the logged-in user.
    Creates a Profile on first access if none exists.
    """
    # Ensure a Profile exists for this user
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={"first_name": request.user.username},
    )
    if created:
        messages.info(
            request,
            "Profile created successfully. Please edit your profile to add more information."
        )

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Update and save the profile
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(
                request,
                f"{request.user.username} profile updated successfully."
            )
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EditProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {"form": form})

# ============Dashboard============
@login_required(login_url="login")
def DashboardPage(request):    
    # Device counts
    total_devices = Device.objects.count()
    online_devices = Device.objects.filter(status='online').count()
    offline_devices = total_devices - online_devices

    # Active alerts (Critical and Warning events from the last 24 hours)
    twenty_four_hours_ago = timezone.now() - timedelta(days=1)
    critical_alerts = Event.objects.filter(
        severity=Event.SavertyChoices.CRITICAL,
        event_date__gte=twenty_four_hours_ago
    ).count()
    warning_alerts = Event.objects.filter(
        severity=Event.SavertyChoices.WARNING,
        event_date__gte=twenty_four_hours_ago
    ).count()
    active_alerts_total = critical_alerts + warning_alerts

    # Monitoring service functions
    def get_network_uptime():
        # Example calculation: In production, replace this with actual monitoring logic.
        # For example, ping devices or aggregate data from various monitoring tools.
    
        return "99.8%"  # This is a placeholder value.

    def get_bandwidth_usage():
        # Example calculation: In production, query your bandwidth monitoring system or SNMP data.
        return "68%"    # This is a placeholder value.

    network_uptime = get_network_uptime()
    bandwidth_usage = get_bandwidth_usage()

    # --- 2. Data for the Recent Events Table ---
    # Get the 5 most recent events, prefetching the related device to avoid extra queries
    recent_events = Event.objects.select_related('device').all()[:5]

    context = {
        'active_page': 'dashboard',
        # Stats card data
        'total_devices': total_devices,
        'online_devices': online_devices,
        'offline_devices': offline_devices,
        'network_uptime': network_uptime,
        'active_alerts_total': active_alerts_total,
        'critical_alerts': critical_alerts,
        'warning_alerts': warning_alerts,
        'bandwidth_usage': bandwidth_usage,
        # Recent events table data
        'recent_events': recent_events,
    }
    return render(request, "users/dashboard.html", context)

# ============404 Page=============
def PageNotFound(request, exception):
    """
    Custom 404 error page view.
    This view is called when a page is not found (404 error).
    It renders a custom 404 error page.
    """
    return render(request, "users/404.html", status=404)