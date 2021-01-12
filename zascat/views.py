from django.shortcuts import render, get_object_or_404
from .models import Prep, PrepImages, PrepCategory, PrepDocs
from django.db.models import Count


def index_cat(request):
    cat_list = PrepCategory.objects.annotate(Count('category'))
    context = {'cat_list': cat_list}
    return render(request, 'zascat/cat_index.html', context)


def index_prep(request, cat_hfu):
    cat_name = get_object_or_404(PrepCategory, cat_hfu=cat_hfu)
    preps_list = Prep.objects.filter(prep_category__name__exact=cat_name)
    context = {'preps_list': preps_list, 'cat_name': cat_name}
    return render(request, 'zascat/prep_list.html', context)


def detail(request, cat_hfu, prep_eng_name):
    catalog = get_object_or_404(PrepCategory, cat_hfu=cat_hfu)
    preps = get_object_or_404(Prep, prep_eng_name=prep_eng_name)
    imgs = PrepImages.objects.filter(prep__prep_name=preps.prep_name)
    docs = PrepDocs.objects.filter(prep_name__prep_name=preps.prep_name)
    return render(request, 'zascat/detail.html', {'preps': preps, 'imgs': imgs, 'catalog': catalog, 'docs': docs})

