"""tests2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, about_view
from cart.views import cart_view
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('articles/', include('blogs.urls')),
    path('account/', include('accounts.urls')),
    path('', home_view, name="home"),
    path('home/', home_view),
    path('about/', about_view),
    path('cart/', include('cart.urls')),
    # path('cart/', )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)