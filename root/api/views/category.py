from ..serializers.category import CategorySerializer
from ecommerce.models import Category

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()


class CategoryRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()
    lookup_field = "slug"