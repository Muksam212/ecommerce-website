from ..views.cart import (
    CartListAPIView,
    CartRetrieveUpdateAPIView, 
    CartListView
)
from django.urls import path

urlpatterns = [
    path('api/cart/list/', CartListAPIView.as_view(), name = 'api-cart-list'),
    path('api/cart/details/<int:id>/', CartRetrieveUpdateAPIView.as_view(), name = 'api-cart-details'),
    path('api/cart/customer/', CartListView.as_view(), name = 'api-cart-customer')
]
