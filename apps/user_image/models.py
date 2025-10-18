from django.db import models
from cloudinary.models import CloudinaryField

from apps.users.models import AuthUser
from apps.images.models import Images

# Create your models here.
class ImagesUser(models.Model):
    user = models.ForeignKey(AuthUser, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, null=True, blank=True, on_delete=models.CASCADE)
    ie_ativo = models.BooleanField(default=False, null=True, blank=True)