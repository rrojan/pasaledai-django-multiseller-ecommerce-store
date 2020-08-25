from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', ]


class RawProductForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    price = forms.DecimalField()
