from django.template import Library
from stories.models import Categories

register = Library()

@register.simple_tag
def get_categories():
    return Categories.objects.all()