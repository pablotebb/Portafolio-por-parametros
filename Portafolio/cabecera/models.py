from django.db import models

# Create your models here.
class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    frase = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to="imagenes", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)