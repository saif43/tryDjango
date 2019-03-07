from django.contrib import admin
from django.urls import path
from .views import (
    product_detail_view,
    product_list_view,
    dynamic_lookup_view,
    delete_product_view,
    product_create_view
)

app_name = 'products'

urlpatterns = [
    path('', product_detail_view, name=''),
    path('allproducts/',product_list_view, name='product-list'),
    path('<int:p_id>', dynamic_lookup_view, name='product-detail'),
    path('delete/<int:p_id>', delete_product_view, name='delete'),
    path('create/', product_create_view, name='create'),
]
