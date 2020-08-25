from django.urls import path
from products.views import product_view, product_create_view, product_pure_create_view, dynamic_lookup_view, product_delete_view, add_to_cart_view


app_name = "products"
urlpatterns = [
    path('', product_view),
    path('<int:id_>/', dynamic_lookup_view, name="product-details"),
    path('<int:id_>/delete/', product_delete_view),
    path('create/', product_create_view),
    path('pure-create/', product_pure_create_view),
    path('<int:id_>/add/', add_to_cart_view),
]
