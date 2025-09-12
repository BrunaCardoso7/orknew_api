from django.contrib.auth.models import AbstractUser
from django.db import models


def uploud_image_profile(instance, filename):
    return f"{instance.id}-{filename}"
def uploud_image_bg(instance, filename):
    return f"{instance.id}-{filename}"

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
    img_profile = models.ImageField(
        upload_to=uploud_image_profile,
        null=True,
        blank=True
    )
    img_background = models.ImageField(
        upload_to=uploud_image_bg,
        null=True,
        blank=True
    )
    ds_bio = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.username
