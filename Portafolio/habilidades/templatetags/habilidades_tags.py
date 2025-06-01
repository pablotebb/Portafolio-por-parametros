from django import template
from ..models import Habilidad
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_habilidades():
    datos = Habilidad.objects.all()  # Traemos los datos del modelo
    return render_to_string('habilidades/habilidades.html', {'datos': datos})