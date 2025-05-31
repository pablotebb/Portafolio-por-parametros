from django import template
from ..models import Personal
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_cabecera():
    datos = Personal.objects.first()  # Traemos los datos del modelo
    return render_to_string('cabecera/cabecera.html', {'datos': datos})