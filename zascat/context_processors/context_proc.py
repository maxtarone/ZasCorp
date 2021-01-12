from django.template.context_processors import request
from zascat.models import PrepCategory


def cat_menu(request):
    return {'cat_list': PrepCategory.objects.all()}
