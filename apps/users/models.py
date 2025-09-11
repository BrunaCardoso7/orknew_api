from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class AuthUser(AbstractUser):
    ROLE_CHOICES = (
        (1, 'admin'),
        (2, 'user')
    )
    role = models.IntegerField(
        choices=ROLE_CHOICES,
        default=2,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
