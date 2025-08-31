import os

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from PIL import Image


def validate_image_file(image):
    """
    Field-level validator to ensure uploaded image is <=5 MB
    and its dimensions don’t exceed 2000×2000.
    """
    max_size = 5 * 1024 * 1024  # 5 MB
    if image.size > max_size:
        raise ValidationError("Image file size should not exceed 5 MB.")

    try:
        img = Image.open(image)
        img_width, img_height = img.size
        if img_width > 2000 or img_height > 2000:
            raise ValidationError("Image dimensions should not exceed 2000×2000 pixels.")
    except ValidationError:
        raise
    except Exception:
        raise ValidationError("Uploaded file is not a valid image.")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            validate_image_file,
        ],
        help_text="Upload a JPEG or PNG up to 5 MB and max 2000×2000px."
    )

    first_name = models.CharField(max_length=100, blank=True)
    last_name  = models.CharField(max_length=100, blank=True)
    bio        = models.TextField(blank=True, max_length=500)
    phone_number = models.CharField(max_length=15, blank=True)
    country    = models.CharField(max_length=100, blank=True)
    city       = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """
        Model-level validation that ties together multiple fields:
        - At least one of first_name/last_name must be provided.
        - Phone number must be digits-only and at least 10 digits.
        """
        super().clean()

        # 1) At least one name
        if not (self.first_name or self.last_name):
            raise ValidationError("At least one of First Name or Last Name must be provided.")

        # 2) Phone number format
        if self.phone_number:
            if not self.phone_number.isdigit():
                raise ValidationError({"phone_number": "Phone number must contain only digits."})
            if len(self.phone_number) < 10:
                raise ValidationError({"phone_number": "Phone number must be at least 10 digits long."})

    def save(self, *args, **kwargs):
        # Run full_clean() so all field validators and clean() get called.
        self.full_clean()

        # Save instance (so we have a self.profile_image.path to work with)
        super().save(*args, **kwargs)

        # Resize the image to max 300×300
        if self.profile_image and os.path.exists(self.profile_image.path):
            try:
                img = Image.open(self.profile_image.path)
                img = img.convert("RGB")
                max_size = (300, 300)
                if img.width > 300 or img.height > 300:
                    img.thumbnail(max_size, Image.ANTIALIAS)
                    img.save(self.profile_image.path, format="JPEG", quality=90)
            except Exception:
                # If resizing fails, fail silently so profile still saves.
                pass

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["created_at"]),
        ]