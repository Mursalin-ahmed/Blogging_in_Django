# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add extra fields here if needed
    phone_number = models.CharField(max_length=15, blank=True, null=True)
