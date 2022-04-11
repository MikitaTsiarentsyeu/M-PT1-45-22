from dataclasses import field
from socket import fromshare
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name' ,'description', 'categories', 'price', 'count', 'photo', 'author']
        widgets = {
            'product_name' : forms.TextInput(attrs={'class': 'form-contol'}),
            'description' : forms.Textarea(attrs={'class': 'form-contol', 'rows': 5,}),
            'categories' : forms.SelectMultiple(attrs={'class': 'form-contol'}),
            'price' : forms.NumberInput(attrs={'class': 'form-contol'}),
            'count' : forms.NumberInput(attrs={'class': 'form-contol'}),
            'photo' : forms.FileInput(attrs={'class': 'form-contol'}),
            'author' : forms.Select(attrs={'class': 'form-contol'})
        }