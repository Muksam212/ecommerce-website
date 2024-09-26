from ..serializers.product import ProductSerializer
from ecommerce.models import Product, Category

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class ProductListAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    model = Product
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    model = Product
    lookup_field = "slug"


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    model = Product

    def get_queryset(self):
        product_slug = self.kwargs.get("slug")
        
        product = self.model.objects.filter(slug = product_slug)

        for obj in product:
            obj.views += 1
            obj.save()
        return product