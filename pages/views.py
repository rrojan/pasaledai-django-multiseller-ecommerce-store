from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html', context={})

def about_view(request):
    return render(request, 'pages/about.html', context={})