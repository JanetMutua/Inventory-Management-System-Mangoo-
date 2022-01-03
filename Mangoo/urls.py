"""Mangoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls
from django.contrib import admin
from django.urls import path, include
#from users.views import LoginFormView
from suppliers.views import SupplierListView
from orders.views import OrderListView
from ItemGroups.views import ItemGroupListView
from Items.views import ItemListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    #path('login/', LoginFormView.as_view(), name='login-page'),
    path('suppliers/', SupplierListView.as_view(), name='supplier-page'),
    # path('register/', include('users.urls')),
    path('orders/', OrderListView.as_view(), name='order-page'),
    path('itemgroup/', ItemGroupListView.as_view(), name='itemgroup-page'),
    # path('profile/', include('users.urls')),
    path('items/', ItemListView.as_view(), name='items-page'),

]
