from django.shortcuts import render
from .models import UserCart
from products.models import Product
from .forms import CheckoutForm
from django.views.generic import CreateView


# Create your views here.

def cart_view(request, id_=1):
    current_user = request.user
    user_id = current_user.id

    usercart = UserCart.objects.get(title="User cart")
    print(usercart.items)

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

def checkout_view(request):
    my_form = CheckoutForm()
    if request.method == 'POST':
        my_form = CheckoutForm(request.POST)
        if my_form.is_valid():
            try:
                CheckoutForm.objects.create(**my_form.cleaned_data)
                my_form = CheckoutForm(request.POST or None)
            except:
                my_form = CheckoutForm(request.POST or None)
    context = {
        'form': my_form
    }
    return render(request, 'cart/checkout.html', context)

class CheckoutView(CreateView):
    template_name = 'blogs/create.html'
    queryset = None
    form_class = CheckoutForm

    