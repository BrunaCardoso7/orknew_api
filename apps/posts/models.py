from django.db import models

from apps.users.models import AuthUser


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE
    )
    nm_descricao = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    dt_created_at = models.DateField(auto_now_add=True)
    dt_updated_at = models.DateField(auto_now=False, blank=True, null=True)
    dt_deleted_at = models.DateField(auto_now=False, blank=True, null=True)
    nm_user_create = models.CharField(max_length=100, blank=True, null=True)
    nm_user_update = models.CharField(max_length=100, blank=True, null=True)
    nm_user_delete = models.CharField(max_length=100, blank=True, null=True)