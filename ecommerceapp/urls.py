from django.urls import path
from .views import *


app_name = "ecommerceapp"
urlpatterns = [
    path("", Homeview.as_view(), name="home"),
    path("signup/", registerview.as_view(), name="signup"),
    path("login/", loginview.as_view(), name="login"),
    path("aboutus/", Aboutusview.as_view(), name='aboutus'),
    path("allproduct/", Allproduct.as_view(), name='allprodudct'),
    path("add-to-cart<int:pro_id>/", Addtocart.as_view(), name='addtocart'),

    path("mycart/", mycart.as_view(), name="mycart"),
    path("manage-cart<int:cp_id>/", Managecart.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", Checkoutview.as_view(), name="checkout"),
    path("register/", registerview.as_view(), name="register"),


    path("loggout/", loggoutview.as_view(), name="loggout"),
    path("login/", loginview.as_view(), name="login"),


]
