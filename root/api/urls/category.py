from ..views.category import (
    CategoryListAPIView,
    CategoryRetrieveUpdateAPIView
)
from django.urls import path

urlpatterns = [
    path('api/category/list/', CategoryListAPIView.as_view(), name = 'api-category-list'),
    path('api/category/details/<slug:slug>/', CategoryRetrieveUpdateAPIView.as_view(), name = 'api-category-details')
]
