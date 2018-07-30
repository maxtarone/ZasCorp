from django.urls import path

from . import views

#from zascat.views import PrepsIndexView

app_name = 'zascat'
urlpatterns = [
    path('', views.index_cat, name='index'),
    path('<int:cat_id>/', views.index_prep, name='prep_list'),
    path('<int:cat_id>/<int:prep_id>/', views.detail, name='detail'),
]
