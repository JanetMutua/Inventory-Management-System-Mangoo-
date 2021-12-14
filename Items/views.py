from django.shortcuts import render
from django.http import request

# Create your views here.


def Items(request):
    return render(request, 'Items/items.html')
