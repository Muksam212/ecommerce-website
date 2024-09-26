from django.db import models

from root.utils import BaseModel
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    email_verified = models.BooleanField(default=False)
    user_image = models.ImageField(upload_to="user/images/", null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"