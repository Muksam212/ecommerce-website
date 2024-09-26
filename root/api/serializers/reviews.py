from rest_framework import serializers
from ecommerce.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "product",
            "rating",
            "comment"
        )