from django.contrib import admin

# Register your models here.
from .models import Prep, PrepImages, PrepCategory, PrepDocs

admin.site.register(Prep)
admin.site.register(PrepImages)
admin.site.register(PrepCategory)
admin.site.register(PrepDocs)
