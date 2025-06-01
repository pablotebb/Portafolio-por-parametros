from django import template
from ..models import Hobby

from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_aficiones():
    datos = Hobby.objects.all()  # Traemos todos los datos del modelo
    return render_to_string('aficiones/aficiones.html', {'datos': datos})