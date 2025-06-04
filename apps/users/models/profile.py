# ===========Importing Required Libraries and Modules=========================
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from PIL import Image
import os
# -----------------------------------------------------------------------------

# Custom validator for image size and dimensions
def Image_Validator(image):
    # Validate the image size and format
    max_size = 5 * 1024 * 1024  # 5 MB
    if image.size > max_size:
        raise ValidationError(f"Image file size should not exceed {max_size / (1024 * 1024)} MB.")

    # Validate the image dimensions
    try:
        img = Image.open(image)
        max_width , max_hight = 2000 , 2000
        if img.width > max_width or img.height > max_hight:
            raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_hight} pixels.")
    except Exception as e:
        raise ValidationError(f"Invalid image format: {e}")


# =================Profile Model========================================
# This model is used to create a profile for the user.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True , verbose_name="Profile Image" ,
                                      help_text="Upload a profile image",
                                      validators=[
                                          FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
                                          Image_Validator 
                                        ])
    
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True , max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    # save method to resize image after upload
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_image and os.path.isfile(self.profile_image.path):
            try:
                img = Image.open(self.profile_image.path) # Open the image file
                img = img.convert("RGB") # Convert the image to RGB mode if not already
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size) # Resize the image to fit within 300x300 pixels
                    img.save(self.profile_image.path, format=img.format) # Save the resized image
                img.close() 
            except Exception as e:
                raise ValidationError(f"Error processing image: {e}")
            
        if self.phone_number and not self.phone_number.isdigit():
            raise ValidationError(
                "Phone number must contain only digits."
            )
        if self.phone_number and len(self.phone_number) < 10:
            raise ValidationError(
                "Phone number must be at least 10 digits long."
            )
    class Meta:
        # class meta for customizing the admin interface
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]

        # Define indexes for the model
        # This is optional but can help with query performance
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["created_at"]),
        ]
