from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('product',views.product,name="product"),
    path('sucess_home',views.home,name="sucess_home"),
    path('product_payment/<int:id>',views.product_payment,name="product"),
    path('home',views.home,name="home"),
]
