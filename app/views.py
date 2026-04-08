from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Supermarket,
    Section,
    Employee,
    Product,
    Warehouse,
    Distributor,
    Client,
    Purchase,
    Order,
    WareHStock,
)
from .forms import SupermarketForm, SectionForm, EmployeeForm, ProductForm, WarehouseForm, DistributorForm, ClientForm, PurchaseForm, OrderForm

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
    products = Product.objects.select_related('section_name').all()
    return render(request, 'product_list.html', {'products': products})

def warehouse_list(request):
    warehouses = Warehouse.objects.select_related('supermarket').all()
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

def supermarket_create(request):
    if request.method == 'POST':
        form = SupermarketForm(request.POST)
        if form.is_valid():
            sections = form.cleaned_data.pop('sections')
            obj = Supermarket.objects.create(**form.cleaned_data)
            if sections is not None:
                obj.sections.set(sections)
            return redirect('supermarket_list')
    else:
        form = SupermarketForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Supermarket', 'icon': 'bi-shop', 'list_url': 'supermarket_list'})

def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            Section.objects.create(**form.cleaned_data)
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Section', 'icon': 'bi-tags', 'list_url': 'section_list'})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            Employee.objects.create(**form.cleaned_data)
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Employee', 'icon': 'bi-person-badge', 'list_url': 'employee_list'})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Product', 'icon': 'bi-box-seam', 'list_url': 'product_list'})

def warehouse_create(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            products = form.cleaned_data.pop('products', [])
            obj = Warehouse.objects.create(**form.cleaned_data)
            from .models import WareHStock
            for prod in products:
                WareHStock.objects.create(warehouse=obj, product=prod, wqty=0)
            return redirect('warehouse_list')
    else:
        form = WarehouseForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Warehouse', 'icon': 'bi-boxes', 'list_url': 'warehouse_list'})

def distributor_create(request):
    if request.method == 'POST':
        form = DistributorForm(request.POST)
        if form.is_valid():
            Distributor.objects.create(**form.cleaned_data)
            return redirect('distributor_list')
    else:
        form = DistributorForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Distributor', 'icon': 'bi-building', 'list_url': 'distributor_list'})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            Client.objects.create(**form.cleaned_data)
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Client', 'icon': 'bi-emoji-smile', 'list_url': 'client_list'})

def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            products = form.cleaned_data.pop('products', [])
            obj = Purchase.objects.create(**form.cleaned_data)
            from .models import PurchaseItem
            for prod in products:
                PurchaseItem.objects.create(purchase=obj, product=prod, quantity=1, price_at_purchase=prod.price)
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Purchase', 'icon': 'bi-receipt', 'list_url': 'purchase_list'})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            products = form.cleaned_data.pop('products', [])
            obj = Order.objects.create(**form.cleaned_data)
            from .models import OrderItem
            for prod in products:
                OrderItem.objects.create(order=obj, product=prod, quantity=1)
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'generic_form.html', {'form': form, 'title': 'Add Order', 'icon': 'bi-truck', 'list_url': 'order_list'})

def supermarket_detail(request, pk):
    item = get_object_or_404(Supermarket, pk=pk)
    fields = {
        'ID': item.id,
        'Location': item.location,
        'Opening Time': item.opening_time,
        'Closing Time': item.close_time,
        'Sections included': ", ".join([s.sname for s in item.sections.all()]) or 'None'
    }
    return render(request, 'generic_detail.html', {'title': 'Supermarket Details', 'icon': 'bi-shop', 'list_url': 'supermarket_list', 'fields': fields})

def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    products = Product.objects.filter(section_name=section).order_by('name')
    return render(
        request,
        'section_detail.html',
        {'section': section, 'products': products},
    )

def employee_detail(request, pk):
    item = get_object_or_404(Employee, pk=pk)
    fields = {
        'Employee Number': item.enumber,
        'Name': item.name,
        'Role': item.role,
        'Salary': f"{item.salary} €",
        'Age': item.age,
        'Contact': item.contact,
        'Supermarket': item.supermarket.location,
        'Sex': item.get_sex_display(),
        'Supervisor': item.supervisor.name if item.supervisor else 'None'
    }
    return render(request, 'generic_detail.html', {'title': 'Employee Details', 'icon': 'bi-person-badge', 'list_url': 'employee_list', 'fields': fields})

def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related('section_name'),
        pk=pk,
    )
    stock_rows = (
        WareHStock.objects.filter(product=product)
        .select_related('warehouse', 'warehouse__supermarket')
        .order_by('warehouse__wnumber')
    )
    return render(
        request,
        'product_detail.html',
        {
            'product': product,
            'stock_rows': stock_rows,
        },
    )

def warehouse_detail(request, pk):
    warehouse = get_object_or_404(
        Warehouse.objects.select_related('supermarket'),
        pk=pk,
    )
    stock_rows = (
        WareHStock.objects.filter(warehouse=warehouse)
        .select_related('product', 'product__section_name')
        .order_by('product__name')
    )
    return render(
        request,
        'warehouse_detail.html',
        {'warehouse': warehouse, 'stock_rows': stock_rows},
    )

def distributor_detail(request, pk):
    item = get_object_or_404(Distributor, pk=pk)
    fields = {
        'Name': item.name,
        'Email': item.email,
        'Contact': item.contact or 'N/A'
    }
    return render(request, 'generic_detail.html', {'title': 'Distributor Details', 'icon': 'bi-building', 'list_url': 'distributor_list', 'fields': fields})

def client_detail(request, pk):
    item = get_object_or_404(Client, pk=pk)
    fields = {
        'NIF': item.nif,
        'Name': item.name or 'N/A',
        'Fidelity Points': item.fidelity or '0',
        'Address': item.address or 'N/A',
        'Contact': item.contact or 'N/A'
    }
    return render(request, 'generic_detail.html', {'title': 'Client Details', 'icon': 'bi-emoji-smile', 'list_url': 'client_list', 'fields': fields})

def purchase_detail(request, pk):
    item = get_object_or_404(Purchase, pk=pk)
    
    # Calculate details of purchase
    items = item.purchaseitem_set.all()
    products_details = [f"{p_item.quantity}x {p_item.product.name} (at {p_item.price_at_purchase}€ each)" for p_item in items]
    
    fields = {
        'Purchase ID': item.purchid,
        'Date': item.date.strftime("%Y-%m-%d %H:%M"),
        'Supermarket': item.supermarket.location,
        'Client': item.client.name if item.client else 'Anonymous',
        'Total Cost': f"{item.calculated_total} €",
        'Products Bought': "\n".join(products_details) or 'No items'
    }
    return render(request, 'generic_detail.html', {'title': 'Purchase Details', 'icon': 'bi-receipt', 'list_url': 'purchase_list', 'fields': fields})

def order_detail(request, pk):
    item = get_object_or_404(Order, pk=pk)
    
    items = item.orderitem_set.all()
    products_details = [f"{o_item.quantity}x {o_item.product.name}" for o_item in items]
    
    fields = {
        'Order ID': item.orderid,
        'Order Date': item.ord_date.strftime("%Y-%m-%d"),
        'Supermarket': item.supermarket.location,
        'Distributor': item.distributor.name,
        'Total Order Cost': f"{item.ord_total} €",
        'Products Ordered': "\n".join(products_details) or 'No items'
    }
    return render(request, 'generic_detail.html', {'title': 'Order Details', 'icon': 'bi-truck', 'list_url': 'order_list', 'fields': fields})
