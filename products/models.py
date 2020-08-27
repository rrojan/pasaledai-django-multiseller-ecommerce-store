from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    summary = models.TextField(blank=True, null=True, max_length=150)
    featured = models.BooleanField(default=False)
    thumb = models.ImageField(upload_to='products/media', default='default.png', blank=True)
    seller = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    date = models.DateField(default=None)

    def get_absolute_url(self):
        # return f"/products/{self.id}/"
        return reverse("products:product-details", kwargs={"id_": self.id})

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:40] + '...'

    def snippet2(self):
        return self.description[:120] + '...'




class InviteCode(models.Model):
    invite_code = models.DecimalField(max_digits=4, decimal_places=0)


