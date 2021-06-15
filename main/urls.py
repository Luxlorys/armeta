from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete', views.complete, name='complete'),
    path('show_cart', views.show_cart, name='show_cart'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('catalog', views.catalog, name='catalog'),
    path('success', views.success, name='success'),
    path('checkout', views.checkout, name='checkout'),
]