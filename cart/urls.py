from django.urls import path
from cart.views import cart_view, checkout_view, CheckoutView


app_name = "cart"
urlpatterns = [
    path('', cart_view),
    path('checkout/', checkout_view),
    path('<int:id_>', cart_view)
]
