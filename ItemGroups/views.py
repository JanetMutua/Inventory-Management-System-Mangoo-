from ItemGroups.models import ItemGroup
from django.shortcuts import render
from django.http import request
from django.views.generic import ListView

# Create your views here.


class ItemGroupListView(ListView):
    model = ItemGroup
    context_object_name = 'itemgroup'
    template_name = 'ItemGroups/index.html'
