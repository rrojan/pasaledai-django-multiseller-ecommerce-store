from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['first_name', 'middle_name', 'last_name', 'address', 'phone_number']