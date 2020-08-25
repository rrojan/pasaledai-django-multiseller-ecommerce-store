from django.urls import path
from cart.views import cart_view


app_name = "cart"
urlpatterns = [
    path('<int:id_>/', cart_view),
]
