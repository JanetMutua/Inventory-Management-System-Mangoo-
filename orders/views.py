from django.shortcuts import render
from django.http import request
from .models import order
from django.views.generic import ListView


# Create your views here.

class OrderListView(ListView):
    model = order
    context_object_name = 'orders'
    template_name = 'orders/index.html'
