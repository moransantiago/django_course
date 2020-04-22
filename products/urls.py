from django.urls import path

from products.views import (
    product_list_view,
    product_detail_view,
    product_create_view,
    product_update_view,
    product_delete_view
)

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:id>/', product_detail_view, name='product_detail'),
    path('create/', product_create_view, name='product_create'),
    path('update/<int:id>/', product_update_view, name='product_update'),
    path('delete/<int:id>/', product_delete_view, name='product_delete'),
]
