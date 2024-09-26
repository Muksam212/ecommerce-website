from ..views.product import (
    ProductListAPIView,
    ProductDetailsAPIView, 
    ProductListView
)
from django.urls import path

urlpatterns = [
    path('api/product/list/', ProductListAPIView.as_view(), name = 'api-product-list'),
    path('api/product/details/<slug:slug>/', ProductDetailsAPIView.as_view(), name = 'api-product-details'),
    path('api/product/<slug:slug>/', ProductListView.as_view(), name = 'api-product-specific-list')
]
