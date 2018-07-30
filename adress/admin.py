from django.contrib import admin

# Register your models here.
from .models import Sender, Reciever

admin.site.register(Sender)
admin.site.register(Reciever)