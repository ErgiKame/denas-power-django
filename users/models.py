from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    username = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=64, unique=True)
    phone = models.CharField(max_length=16)



