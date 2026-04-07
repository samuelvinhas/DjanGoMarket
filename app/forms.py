from django import forms
from .models import Supermarket, Section, Employee, Product, Warehouse, Distributor, Client, Purchase, Order

class SectionForm(forms.Form):
    sname = forms.CharField(max_length=64, label='Name')
    department = forms.CharField(max_length=64)

class SupermarketForm(forms.Form):
    id = forms.IntegerField()
    location = forms.CharField(max_length=128)
    opening_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    close_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    sections = forms.ModelMultipleChoiceField(queryset=Section.objects.all(), required=False)

class EmployeeForm(forms.Form):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    enumber = forms.IntegerField(label='Employee Number')
    name = forms.CharField(max_length=64)
    role = forms.CharField(max_length=32)
    salary = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    age = forms.IntegerField(min_value=16)
    contact = forms.CharField(max_length=64)
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    supervisor = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)

class ProductForm(forms.Form):
    prodid = forms.IntegerField(label='Product ID')
    name = forms.CharField(max_length=128)
    brand = forms.CharField(max_length=64)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    req_cold = forms.BooleanField(required=False, label='Requires Cold Storage')
    section_name = forms.ModelChoiceField(queryset=Section.objects.all())

class WarehouseForm(forms.Form):
    wnumber = forms.IntegerField(label='Warehouse Number')
    area = forms.CharField(max_length=64)
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

class DistributorForm(forms.Form):
    email = forms.EmailField()
    contact = forms.CharField(max_length=64, required=False)
    name = forms.CharField(max_length=128)

class ClientForm(forms.Form):
    nif = forms.IntegerField(label='NIF')
    name = forms.CharField(max_length=64, required=False)
    fidelity = forms.IntegerField(required=False)
    address = forms.CharField(max_length=128, required=False)
    contact = forms.CharField(max_length=64, required=False)

class PurchaseForm(forms.Form):
    purchid = forms.IntegerField(label='Purchase ID')
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

class OrderForm(forms.Form):
    orderid = forms.IntegerField(label='Order ID')
    ord_total = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    ord_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    distributor = forms.ModelChoiceField(queryset=Distributor.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)