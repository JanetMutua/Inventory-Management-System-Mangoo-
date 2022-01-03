from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


# class dashboard_view(ListView):
def dashboard(request):
    return render(request, 'dashboard/index.html')
