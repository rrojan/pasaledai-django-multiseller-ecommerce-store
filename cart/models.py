from django.db import models
from django.conf import settings
from products.models import Product
from django.shortcuts import redirect
# Create your models here.


class UserCart(models.Model):
    title = models.CharField(max_length=100)
    items = list()
    uid = int()

    def get_absolute_url(self):
        # return f"/products/{self.id}/"
        return reverse("products:product-details", kwargs={"id_": self.id})

    # def __init__(self,userid):
    #     uid = userid

    def __str__(self):
        return self.title

    def return_items(self):
        if len(items) == 0:
            return ["Oh no, looks like your cart is empty :'("]
        else:
            return items 

    def snippet(self):
        return self.description[:40] + '...'    

class Checkout(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def get_absolute_url(self):
        # return f"/products/{self.id}/"
        return redirect(to='/')