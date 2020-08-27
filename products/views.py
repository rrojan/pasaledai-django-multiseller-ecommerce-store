from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm
from django.contrib.auth.models import User
from cart.models import UserCart


# Create your views here.
def product_view(request):
    context = {
        'products': list(Product.objects.all())
    }
    return render(request, 'products/product.html', context)


def dynamic_lookup_view(request, id_):
    # print(id_)
    # obj = get_object_or_404(Product, id=id_)
    try:
        obj = Product.objects.get(id=id_)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        print("form saved")
        form.save()
        form = ProductForm()
    else:
        print("Error!")
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context)


def product_delete_view(request, id_):
    obj = get_object_or_404(Product, id=id_)
    if request.method == "POST":
        obj.delete()
        # product_view(request)
    context = {
        'object': obj
    }
    return render(request, 'products/delete.html', context)


def product_pure_create_view(request):
    print('pure-create view')
    my_form = RawProductForm()
    print(request.method, "1")
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        print(request.method, "2")
        if my_form.is_valid():
            print(request.method, "3")
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm(request.POST or None)
    print(request.method, "4")
    context = {
        'form': my_form
    }
    return render(request, 'products/pure_create.html', context)


def add_to_cart_view(request, id_):
    obj = get_object_or_404(Product, id=id_)
    current_user = request.user
    user_id = current_user.id
    print(user_id)
    


    usercart = UserCart.objects.get(title="User cart")
    
    
    usercart.items.append({'product': Product.objects.get(id=id_), 'userid': user_id})

    total = 0

    for item in usercart.items:
        if user_id == item['userid']:
            p = item['product']
            print(p)
            total += p.price

    context = {
        'user_id':user_id,
        'cart': usercart,
        'total': total,

    }

    return render(request, 'cart/cart.html', context)
