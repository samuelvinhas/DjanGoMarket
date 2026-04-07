from django import forms
from .models import Supermarket, Section, Employee, Product, Warehouse, Distributor, Client, Purchase, Order

class SectionForm(forms.Form):
    sname = forms.CharField(max_length=64, label='Name')
    department = forms.CharField(max_length=64)

    def clean_sname(self):
        sname = self.cleaned_data.get('sname')
        if sname and Section.objects.filter(sname=sname).exists():
            raise forms.ValidationError('A section with this name already exists.')
        return sname

class SupermarketForm(forms.Form):
    id = forms.IntegerField()
    location = forms.CharField(max_length=128)
    opening_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    close_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    sections = forms.ModelMultipleChoiceField(queryset=Section.objects.all(), required=False)

    def clean_id(self):
        id_val = self.cleaned_data.get('id')
        if id_val and Supermarket.objects.filter(id=id_val).exists():
            raise forms.ValidationError('A supermarket with this ID already exists.')
        return id_val

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

    def clean_enumber(self):
        enumber = self.cleaned_data.get('enumber')
        if enumber and Employee.objects.filter(enumber=enumber).exists():
            raise forms.ValidationError('An employee with this number already exists.')
        return enumber

class ProductForm(forms.Form):
    prodid = forms.IntegerField(label='Product ID')
    name = forms.CharField(max_length=128)
    brand = forms.CharField(max_length=64)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    req_cold = forms.BooleanField(required=False, label='Requires Cold Storage')
    section_name = forms.ModelChoiceField(queryset=Section.objects.all())

    def clean_prodid(self):
        prodid = self.cleaned_data.get('prodid')
        if prodid and Product.objects.filter(prodid=prodid).exists():
            raise forms.ValidationError('A product with this ID already exists.')
        return prodid

class WarehouseForm(forms.Form):
    wnumber = forms.IntegerField(label='Warehouse Number')
    area = forms.CharField(max_length=64)
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

    def clean_wnumber(self):
        wnumber = self.cleaned_data.get('wnumber')
        if wnumber and Warehouse.objects.filter(wnumber=wnumber).exists():
            raise forms.ValidationError('A warehouse with this number already exists.')
        return wnumber

class DistributorForm(forms.Form):
    email = forms.EmailField()
    contact = forms.CharField(max_length=64, required=False)
    name = forms.CharField(max_length=128)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Distributor.objects.filter(email=email).exists():
            raise forms.ValidationError('A distributor with this email already exists.')
        return email

class ClientForm(forms.Form):
    nif = forms.IntegerField(label='NIF')
    name = forms.CharField(max_length=64, required=False)
    fidelity = forms.IntegerField(required=False)
    address = forms.CharField(max_length=128, required=False)
    contact = forms.CharField(max_length=64, required=False)

    def clean_nif(self):
        nif = self.cleaned_data.get('nif')
        if nif and Client.objects.filter(nif=nif).exists():
            raise forms.ValidationError('A client with this NIF already exists.')
        return nif

class PurchaseForm(forms.Form):
    purchid = forms.IntegerField(label='Purchase ID')
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

    def clean_purchid(self):
        purchid = self.cleaned_data.get('purchid')
        if purchid and Purchase.objects.filter(purchid=purchid).exists():
            raise forms.ValidationError('A purchase with this ID already exists.')
        return purchid

class OrderForm(forms.Form):
    orderid = forms.IntegerField(label='Order ID')
    ord_total = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    ord_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    distributor = forms.ModelChoiceField(queryset=Distributor.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

    def clean_orderid(self):
        orderid = self.cleaned_data.get('orderid')
        if orderid and Order.objects.filter(orderid=orderid).exists():
            raise forms.ValidationError('An order with this ID already exists.')
        return orderid