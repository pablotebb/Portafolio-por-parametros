from django import template
from ..models import Card, Carrousel

from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_portfolio():
    datos = Card.objects.all().prefetch_related('carrousel')  # Más eficiente
    return render_to_string('portfolio/portfolio.html', {'datos': datos})