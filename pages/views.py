from django.shortcuts import render
from products.models import Product
from blogs.models import Article


# Create your views here.
def home_view(request):
    products = Product.objects.all()[:3]
    articles = Article.objects.all()[:5]
    return render(request, 'pages/home.html', context={'products': products, 'articles': articles,})

def about_view(request):
    return render(request, 'pages/about.html', context={})