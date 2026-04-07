"""
URL configuration for DjanGoMarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('supermarkets/', views.supermarket_list, name='supermarket_list'),
    path('sections/', views.section_list, name='section_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('products/', views.product_list, name='product_list'),
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('distributors/', views.distributor_list, name='distributor_list'),
    path('clients/', views.client_list, name='client_list'),
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('orders/', views.order_list, name='order_list'),

    path('supermarkets/add/', views.supermarket_create, name='supermarket_create'),
    path('sections/add/', views.section_create, name='section_create'),
    path('employees/add/', views.employee_create, name='employee_create'),
    path('products/add/', views.product_create, name='product_create'),
    path('warehouses/add/', views.warehouse_create, name='warehouse_create'),
    path('distributors/add/', views.distributor_create, name='distributor_create'),
    path('clients/add/', views.client_create, name='client_create'),
    path('purchases/add/', views.purchase_create, name='purchase_create'),
    path('orders/add/', views.order_create, name='order_create'),
]
