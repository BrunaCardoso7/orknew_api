from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


def upload_image_profile(instance, filename):
    return f"{instance.id}-profile-{filename}"

def upload_image_bg(instance, filename):
    return f"{instance.id}-bg-{filename}"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class AuthUser(AbstractUser):
    username = None  # removemos o campo username
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # não pede username no createsuperuser

    objects = UserManager()

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
        upload_to=upload_image_profile,
        null=True,
        blank=True
    )
    img_background = models.ImageField(
        upload_to=upload_image_bg,
        null=True,
        blank=True
    )
    ds_bio = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email
