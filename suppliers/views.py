from django.shortcuts import render
from django.http import request


def suppliers(request):
    return render(request, 'suppliers/index.html')
