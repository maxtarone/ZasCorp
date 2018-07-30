from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

# Create your views here.
from .models import Sender

class IndexView(generic.ListView):
    template_name = 'adress/envelope.svg'
    context_object_name = 'latest_sender_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Sender.objects.order_by('-from_name')[:1]
