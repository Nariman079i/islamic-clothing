from django import template
from ..models import *

register = template.Library()

@register.simple_tag()
def clo_tags():
    return Clothing.objects.all()


