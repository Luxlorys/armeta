from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog_max', views.catalog_max, name='catalog_max'),
    path('complete', views.complete, name='complete')
]