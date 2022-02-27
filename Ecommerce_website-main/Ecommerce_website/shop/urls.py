from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="about"),
    path('products/<int:myId>', views.productView, name="productView"),
    path('contact/', views.contactUs, name="contactUs"),
    path('tracker/', views.tracker, name="tracker"),
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cartPage, name="cart"),
]
