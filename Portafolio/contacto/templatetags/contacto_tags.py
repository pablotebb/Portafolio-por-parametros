from django import template
from ..models import Contacto

from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_contacto():
    datos = Contacto.objects.all()  # Traemos todos los datos del modelo
    return render_to_string('contacto/contacto.html', {'datos': datos})