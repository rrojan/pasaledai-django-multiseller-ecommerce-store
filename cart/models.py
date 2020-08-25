from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.


class UserCart(models.Model):
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