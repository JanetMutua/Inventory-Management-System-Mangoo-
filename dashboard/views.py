from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD

def dashboard(request):
    return render(request, 'dashboard/index.html')
=======
# Create your views here.os.path.join(BASE_DIR, 'templates')


def dashboard(request):
    return render(request, 'dashboard/base.html')
>>>>>>> 90fb56f4da6699a7c6e0cfa2d972624e44299b28
