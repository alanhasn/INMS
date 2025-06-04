# ===========Importing Required Libraries and Modules=========================
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm # built in userCreation form
from django import forms 
from .models import Profile
# ------------------------------------------------------------------------------

# This form is used to create a new user.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User  
        fields = ["username","email","password1","password2"] # show this field in the template

# This form is used to authenticate a user.
class AuthenticationUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150 , widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

# this form is used to edit the profile of the user.
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [  # fields to be shown in the template
            "profile_image",
            "first_name",
            "last_name",
            "bio", 
            "phone_number",
            "city" ,
            "country",
]

        # widgets are used to customize the form fields
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write something about you...", "rows": 4}),
            "phone_number": forms.TextInput( attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
            "country": forms.TextInput(attrs={"class": "form-control", "placeholder": "Country"}),
            "profile_image": forms.FileInput(attrs={"class": "form-control-file"}),
        }
