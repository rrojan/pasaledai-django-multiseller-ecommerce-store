# from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from products.invite_codes import seller_invite_codes
from cart.models import UserCart


class CustomerUserCreationForm(UserCreationForm):
    seller = False


class SellerUserCreationForm(UserCreationForm):
    seller = True
    invite_code = forms.DecimalField(max_digits=4, max_value=9999)
    
    def clean_invite_code(self, *args, **kwargs):
        inv = self.cleaned_data.get("invite_code")

        if inv in seller_invite_codes:
            return inv
        else:
            raise forms.ValidationError("Invalid invite code!")

