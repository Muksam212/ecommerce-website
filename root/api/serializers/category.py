from rest_framework import serializers
from ecommerce.models import Category

from ..serializers.product import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    #nested serializers
    product_category = ProductSerializer(many = True)
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "product_category")