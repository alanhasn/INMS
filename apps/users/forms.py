# ===========Importing Required Libraries and Modules=========================
from django import forms
from django.contrib.auth.forms import (  # built in userCreation form
    AuthenticationForm, UserCreationForm)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import (InMemoryUploadedFile,
                                            TemporaryUploadedFile)

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
            "city",
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

    def clean_profile_image(self):
        image = self.cleaned_data.get("profile_image")

        # If user uploaded a new file, validate content_type + size
        if isinstance(image, (InMemoryUploadedFile, TemporaryUploadedFile)):
            # 1) Type
            if image.content_type not in ("image/jpeg", "image/png"):
                raise ValidationError("Only JPEG or PNG images are allowed.")

            # 2) Size (5 MB max)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Image must be smaller than 5 MB.")

        # If it's the existing ImageFieldFile, we skip content_type check
        return image
    

    def clean(self):
        cleaned_data = super().clean()

        # 1) Phone-number validation
        phone_number = cleaned_data.get("phone_number")
        if phone_number:
            if not phone_number.isdigit():
                self.add_error(
                    "phone_number",
                    "Phone number must contain only digits."
                )
            if len(phone_number) < 10:
                self.add_error(
                    "phone_number",
                    "Phone number must be at least 10 digits long."
                )

        # 2) First/Last name cross-field rule
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if not first_name and not last_name:
            raise forms.ValidationError(
                "At least one of First Name or Last Name must be provided."
            )
        if first_name and len(first_name) < 2:
            self.add_error(
                "first_name",
                "First Name must be at least 2 characters long."
            )
        if last_name and len(last_name) < 2:
            self.add_error(
                "last_name",
                "Last Name must be at least 2 characters long."
            )

        # 3) Bio length
        bio = cleaned_data.get("bio")
        if bio and len(bio) > 500:
            self.add_error(
                "bio",
                "Bio should not exceed 500 characters."
            )

        # 4) City/Country length
        city = cleaned_data.get("city")
        if city and len(city) < 2:
            self.add_error(
                "city",
                "City name must be at least 2 characters long."
            )
        country = cleaned_data.get("country")
        if country and len(country) < 2:
            self.add_error(
                "country",
                "Country name must be at least 2 characters long."
            )

        return cleaned_data