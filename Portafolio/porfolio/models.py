from django.db import models



# Create your models here.
class Card(models.Model):
    imagen = models.FileField(
        upload_to="imagenes",
        null=True,
        blank=True,
        default='imagenes/default.jpg'
    )
    enlace_ir_codigo = models.URLField()
    enlace_carrousel = models.CharField()
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Carrousel(models.Model):
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='carrousel'
    )
    id_carrousel = models.CharField(null=True, blank=True)
    slide = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    

    
