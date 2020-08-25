from django.urls import path
from accounts.views import signup_view, login_view, logout_view, seller_signup_view

app_name = "account"
urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('seller-signup/', seller_signup_view, name="seller-signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]
