from django.shortcuts import render
from django.http import request


# Create your views here.


def orders(request):
    return render(request, 'orders/index.html')
