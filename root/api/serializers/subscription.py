from rest_framework import serializers
from ecommerce.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Subscription
        fields = (
            "id",
            "name",
            "email",
            "status"
        )

    def validate_status(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Status must be either True or False")
        return value
    
    def validated_email(self, value):
        if Subscription.objects.filter(email = value).exists():
            raise serializers.ValidationError("A subscription with this email already exists")
        return value