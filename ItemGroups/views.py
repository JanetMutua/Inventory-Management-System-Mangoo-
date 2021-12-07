from django.shortcuts import render
from django.http import request

# Create your views here.


def ItemGroups(request):
    return render(request, 'ItemGroups/index.html')
