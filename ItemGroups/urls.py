from . import views
from django.urls import path

urlpatterns = [
    path('', views.ItemGroups, name='item_group')
]
