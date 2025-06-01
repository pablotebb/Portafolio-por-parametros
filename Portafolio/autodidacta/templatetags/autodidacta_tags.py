from django import template
from ..models import Autodidacta

from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_autodidacta():
    datos = Autodidacta.objects.all()  # Traemos todos los datos del modelo
    return render_to_string('autodidacta/autodidacta.html', {'datos': datos})