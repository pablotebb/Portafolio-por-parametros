from django.db import models

# Create your models here.
class Habilidad(models.Model):
    leyenda = models.CharField(max_length=50)
    foto = models.FileField(upload_to="imagenes", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)