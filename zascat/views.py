from django.shortcuts import render, get_object_or_404
from .models import Prep, PrepImages, PrepCategory


def index_cat(request):
    cat_list = PrepCategory.objects.all()
    context = {'cat_list': cat_list}
    return render(request, 'zascat/index.html', context)


def index_prep(request, cat_id):
    cat_name = get_object_or_404(PrepCategory, pk=cat_id)
    preps_list = Prep.objects.filter(prep_category__name__exact=cat_name)
    context = {'preps_list': preps_list, 'cat_name': cat_name}
    return render(request, 'zascat/prep_list.html', context)


def detail(request, cat_id, prep_id):
    catalog = get_object_or_404(PrepCategory, pk=cat_id)
    preps = get_object_or_404(Prep, pk=prep_id)
    imgs = PrepImages.objects.filter(prep__prep_name=preps.prep_name)
    return render(request, 'zascat/detail.html', {'preps': preps, 'imgs':imgs, 'catalog': catalog})

