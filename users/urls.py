from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login-page')
]


urlpatterns = [
    path('', views.register, name='register-page')
]

urlpatterns = [
    path('', views.profile, name='profile-page')
]
