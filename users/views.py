from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')


def profile(request):
    return render(request, 'users/profile.html')