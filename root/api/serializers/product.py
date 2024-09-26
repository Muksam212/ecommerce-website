from rest_framework import serializers
from ecommerce.models import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "price",
            "stock",
            "category",
            "image",
            "views"
        )