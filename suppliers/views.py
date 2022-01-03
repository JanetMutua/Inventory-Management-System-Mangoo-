from django.shortcuts import render
from django.http import request
from django.views.generic import ListView
from .models import Supplier


class SupplierListView(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'suppliers/index.html'
