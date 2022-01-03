from django.shortcuts import render
from django.http import request
from django.views.generic import ListView
from .models import Item

# Create your views here.


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'Items/index.html'
