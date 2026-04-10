from django import forms
from django.contrib.auth.models import Group
from .models import Supermarket, Section, Employee, Product, Warehouse, Distributor, Client, Purchase, Order

class SectionForm(forms.Form):
    sname = forms.CharField(max_length=64, label='Name')
    department = forms.CharField(max_length=64)

    def __init__(self, *args, is_editing=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        if is_editing:
            self.fields['sname'].widget.attrs['disabled'] = 'disabled'
            self.fields['sname'].widget.attrs['class'] = 'form-control-plaintext'
            self.fields['sname'].required = False

    def clean_sname(self):
        sname = self.cleaned_data.get('sname')
        if not self.is_editing and sname and Section.objects.filter(sname=sname).exists():
            raise forms.ValidationError('A section with this name already exists.')
        return sname

class SupermarketForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    location = forms.CharField(max_length=128)
    opening_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    close_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    sections = forms.ModelMultipleChoiceField(queryset=Section.objects.all(), required=False)

    def __init__(self, *args, is_editing=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing

        if not is_editing:
            del self.fields['id']
        else:
            self.fields['id'].widget = forms.TextInput(attrs={'disabled': 'disabled', 'class': 'form-control-plaintext'})
            self.fields['id'].required = False

class EmployeeForm(forms.Form):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    enumber = forms.IntegerField(label='Employee Number', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    name = forms.CharField(max_length=64)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Group")
    role = forms.CharField(max_length=32)
    salary = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    age = forms.IntegerField(min_value=16)
    contact = forms.CharField(max_length=64)
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    supervisor = forms.ModelChoiceField(queryset=Employee.objects.all(), required=False)

    def __init__(self, *args, is_editing=False, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        self.user = user

        if user and not user.groups.filter(name='CEO').exists():
            self.fields['group'].queryset = Group.objects.exclude(name='CEO')

        if self.user and not self.user.groups.filter(name='CEO').exists():
            self.fields['supermarket'].queryset = Supermarket.objects.filter(id=self.user.supermarket.id)
            self.fields['supermarket'].initial = self.user.supermarket
            self.fields['supermarket'].widget = forms.TextInput(attrs={'readonly': 'readonly'})

        if not is_editing:
            del self.fields['enumber']
        else:
            self.fields['enumber'].widget = forms.TextInput(attrs={'disabled': 'disabled', 'class': 'form-control-plaintext'})
            self.fields['enumber'].required = False

class ProductForm(forms.Form):
    prodid = forms.IntegerField(label='Product ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    name = forms.CharField(max_length=128)
    brand = forms.CharField(max_length=64)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    req_cold = forms.BooleanField(required=False, label='Requires Cold Storage')
    section_name = forms.ModelChoiceField(queryset=Section.objects.all())

    def __init__(self, *args, is_editing=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        if not is_editing:
            del self.fields['prodid']
        else:
            self.fields['prodid'].widget = forms.TextInput(attrs={'disabled': 'disabled', 'class': 'form-control-plaintext'})
            self.fields['prodid'].required = False

    def clean_prodid(self):
        prodid = self.cleaned_data.get('prodid')
        if not self.is_editing and prodid and Product.objects.filter(prodid=prodid).exists():
            raise forms.ValidationError('A product with this ID already exists.')
        return prodid

class WarehouseForm(forms.Form):
    wnumber = forms.IntegerField(label='Warehouse Number', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    area = forms.CharField(max_length=64)
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

    def __init__(self, *args, is_editing=False, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        self.user = user

        if self.user and not self.user.groups.filter(name='CEO').exists():
            self.fields['supermarket'].queryset = Supermarket.objects.filter(id=self.user.supermarket.id)
            self.fields['supermarket'].initial = self.user.supermarket
            self.fields['supermarket'].widget = forms.TextInput(attrs={'readonly': 'readonly'})

        if not is_editing:
            del self.fields['wnumber']
        else:
            self.fields['wnumber'].widget = forms.TextInput(attrs={'disabled': 'disabled', 'class': 'form-control-plaintext'})
            self.fields['wnumber'].required = False

    def clean_wnumber(self):
        wnumber = self.cleaned_data.get('wnumber')
        if not self.is_editing and wnumber and Warehouse.objects.filter(wnumber=wnumber).exists():
            raise forms.ValidationError('A warehouse with this number already exists.')
        return wnumber

class DistributorForm(forms.Form):
    email = forms.EmailField()
    contact = forms.CharField(max_length=64, required=False)
    name = forms.CharField(max_length=128)

    def __init__(self, *args, is_editing=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        if is_editing:
            self.fields['email'].widget.attrs['disabled'] = 'disabled'
            self.fields['email'].widget.attrs['class'] = 'form-control-plaintext'
            self.fields['email'].required = False

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not self.is_editing and email and Distributor.objects.filter(email=email).exists():
            raise forms.ValidationError('A distributor with this email already exists.')
        return email

class ClientForm(forms.Form):
    nif = forms.IntegerField(label='NIF')
    name = forms.CharField(max_length=64, required=False)
    fidelity = forms.IntegerField(required=False)
    address = forms.CharField(max_length=128, required=False)
    contact = forms.CharField(max_length=64, required=False)

    def __init__(self, *args, is_editing=False, client_pk=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        self.client_pk = client_pk

    def clean_nif(self):
        nif = self.cleaned_data.get('nif')
        if not nif:
            raise forms.ValidationError('NIF is required.')
        
        # Check for duplicate NIF
        if nif:
            query = Client.objects.filter(nif=nif)
            if self.is_editing and self.client_pk:
                query = query.exclude(nif=self.client_pk)
            if query.exists():
                raise forms.ValidationError('A client with this NIF already exists.')
        return nif

class PurchaseForm(forms.Form):
    purchid = forms.IntegerField(label='Purchase ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

    def __init__(self, *args, is_editing=False, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        self.user = user
        if self.user and not self.user.groups.filter(name='CEO').exists():
            self.fields['supermarket'].queryset = Supermarket.objects.filter(id=self.user.supermarket.id)
            self.fields['supermarket'].initial = self.user.supermarket
            self.fields['supermarket'].widget = forms.TextInput(attrs={'readonly': 'readonly'})

        if not is_editing:
            del self.fields['purchid']
        else:
            self.fields['purchid'].widget = forms.TextInput(attrs={'disabled': 'disabled', 'class': 'form-control-plaintext'})
            self.fields['purchid'].required = False

    def clean_purchid(self):
        purchid = self.cleaned_data.get('purchid')
        if not self.is_editing and purchid and Purchase.objects.filter(purchid=purchid).exists():
            raise forms.ValidationError('A purchase with this ID already exists.')
        return purchid

class OrderForm(forms.Form):
    orderid = forms.IntegerField(label='Order ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    ord_total = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
    ord_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    supermarket = forms.ModelChoiceField(queryset=Supermarket.objects.all())
    distributor = forms.ModelChoiceField(queryset=Distributor.objects.all())
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), required=False)

    def __init__(self, *args, is_editing=False, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_editing = is_editing
        self.user = user

        if self.user and not self.user.groups.filter(name='CEO').exists():
            self.fields['supermarket'].queryset = Supermarket.objects.filter(id=self.user.supermarket.id)
            self.fields['supermarket'].initial = self.user.supermarket
            self.fields['supermarket'].widget = forms.TextInput(attrs={'readonly': 'readonly'})

        if not is_editing:
            del self.fields['orderid']
        else:
            self.fields['orderid'].widget = forms.TextInput(attrs={'disabled': 'disabled', 'class': 'form-control-plaintext'})
            self.fields['orderid'].required = False

    def clean_orderid(self):
        orderid = self.cleaned_data.get('orderid')
        if not self.is_editing and orderid and Order.objects.filter(orderid=orderid).exists():
            raise forms.ValidationError('An order with this ID already exists.')
        return orderid
