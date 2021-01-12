from django.urls import path

from . import views

#from zascat.views import PrepsIndexView

app_name = 'zascat'
urlpatterns = [
    path('', views.index_cat, name='index'),
    path('<cat_hfu>/', views.index_prep, name='prep_list'),
    path('<cat_hfu>/<prep_eng_name>/', views.detail, name='detail'),
]
