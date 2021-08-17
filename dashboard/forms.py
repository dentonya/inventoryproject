from django import forms
from .models import Product, Order, Supplier


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'category', 'quantity', 'company']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity', 'customer', 'amount']

