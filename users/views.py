from django.shortcuts import render
from django.http import request
from .models import Profile
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
# Create your views here.


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.

    else:
        # Return an 'invalid login' error message.
        return 'Valid login credentials'


def register(request):
    return render(request, 'users/register.html')


def profile(request):
    return render(request, 'users/profile.html')
