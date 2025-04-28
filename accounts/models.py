from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos adicionales si los necesitas
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.username