# ===================Imports===================
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages # Message framework
from ..forms import CreateUserForm, AuthenticationUserForm, EditProfileForm # My Custom Form
from ..models import Profile # My Custom Model
from django.views import View

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
                return redirect("profile") 
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
    profile, created = Profile.objects.get_or_create(user=request.user) # Get the user profile

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
    profile, created = Profile.objects.get_or_create(user=request.user) 
    
    if created:
        messages.info(request, "Profile created successfully. Please edit your profile to add more information.")

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile) # get the form data and instance of the profile
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, f"{request.user} Profile updated successfully.")
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile) # if its not valid form return empty form
    # context data
    context = {
        "form":form
    }
    return render(request, "users/edit_profile.html", context)

# ============Dashboard============
@login_required(login_url="login")
def DashboardPage(request):    
    return render(request, "users/dashboard.html")

    
# ============404 Page=============
def PageNotFound(request, exception):
    """
    Custom 404 error page view.
    This view is called when a page is not found (404 error).
    It renders a custom 404 error page.
    """
    return render(request, "users/404.html", status=404)
