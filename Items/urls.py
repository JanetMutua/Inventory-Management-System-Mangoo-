from django.urls import path
from . import views


urlpatterns = [
    path('', views.Items, name='items-page')
]
