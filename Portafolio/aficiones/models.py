from django.db import models

# Create your models here.
class Hobby(models.Model):
    descripcion = models.TextField()
    foto = models.FileField(upload_to="imagenes", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)