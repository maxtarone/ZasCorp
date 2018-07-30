from django.contrib import admin

# Register your models here.
from .models import Prep, PrepImages, PrepCategory

admin.site.register(Prep)
admin.site.register(PrepImages)
admin.site.register(PrepCategory)
