from django import template
from zascat.models import PrepCategory

register = template.Library()

@register.inclusion_tag('cat_menu.html')
def cat_menu():
    cat_list = PrepCategory.objects.all()
    return {'cat_list': cat_list}
