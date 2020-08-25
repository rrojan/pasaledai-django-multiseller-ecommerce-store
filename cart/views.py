from django.shortcuts import render
from .models import UserCart


# Create your views here.

def cart_view(request, id_):
    current_user = request.user
    user_id = current_user.id

    try:
        usercart = UserCart.objects.get(uid=user_id)
    except:
        usercart = UserCart()
        usercart.uid = user_id

    context = {
        'user_id':user_id,
        'cart': usercart,

    }
    return render(request, 'cart/cart.html', context)
