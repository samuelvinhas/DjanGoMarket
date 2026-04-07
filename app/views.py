from django.shortcuts import render
from .models import Supermarket, Section, Employee, Product, Warehouse, Distributor, Client, Purchase, Order

def home(request):
    return render(request, 'home.html')

def supermarket_list(request):
    supermarkets = Supermarket.objects.all()
    return render(request, 'supermarket_list.html', {'supermarkets': supermarkets})

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'section_list.html', {'sections': sections})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse_list.html', {'warehouses': warehouses})

def distributor_list(request):
    distributors = Distributor.objects.all()
    return render(request, 'distributor_list.html', {'distributors': distributors})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase_list.html', {'purchases': purchases})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
