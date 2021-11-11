from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.os.path.join(BASE_DIR, 'templates')


def dashboard(request):
    return render(request, 'dashboard/base.html')
