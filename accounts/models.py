# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # add additional fields in here

    def __str__(self):
        return self.username