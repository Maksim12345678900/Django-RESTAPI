from django.urls import path
from .views import WarehouseList, WarehouseDetail, ProductList, ProductDetail

urlpatterns = [
    path('warehouses/', WarehouseList.as_view(), name='warehouse-list'),
    path('warehouses/<int:pk>/', WarehouseDetail.as_view(), name='warehouse-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
