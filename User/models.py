from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username=models.CharField(max_length=5, unique=True)
    USERNAME_FIELD = "username"

