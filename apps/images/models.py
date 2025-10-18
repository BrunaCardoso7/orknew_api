from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Images(models.Model):
    ORIGEM_IMAGEM = (
        ("PRF", "PERFIL"),
        ("PFF", "PERFIL_FUNDO"),
        ("PST", "POSTAGEM")
    )

    title = models.CharField(max_length=255)
    image = CloudinaryField('image', folder='images')
    ie_origem = models.CharField(
        choices=ORIGEM_IMAGEM,
        null=True,
        blank=True,
        max_length=255
    )