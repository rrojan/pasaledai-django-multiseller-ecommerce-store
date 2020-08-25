from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SellerUserCreationForm, CustomerUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def seller_signup_view(request):
    if request.method == 'POST':
        form = SellerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SellerUserCreationForm()
    return render(request, 'accounts/seller_signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', context={'form': form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)

        return redirect('/')
    else:
        pass
