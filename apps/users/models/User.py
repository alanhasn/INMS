# Create Custome user model
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add custom fields here
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        Manager = 'MANAGER', 'Manager'
        Employee = 'EMPLOYEE', 'Employee'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.Employee)

    def __str__(self):
        return self.username
