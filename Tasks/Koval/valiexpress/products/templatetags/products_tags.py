from django import template

from products.models import Category
from advertisement.models import Advertisement 

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def get_adverisements():
    return Advertisement.objects.all()