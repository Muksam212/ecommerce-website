from rest_framework import serializers
from users.models import User
from ecommerce.models import Customer

class CustomerRegistration(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password")

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
    
    # Override the create method to handle password hashing
    def create(self, validated_data):
        # Remove the password2 field from validated data as it's not needed for creation
        validated_data.pop('confirm_password')

        # Create a new user instance
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password = validated_data['password'],
        )
        
        # Set the password (hashing it)
        user.set_password(validated_data['password'])

        Customer.objects.create(user = user)
        
        # Save the user to the database
        user.save()

        return user
    

class CustomerListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = "user.username", read_only = True)
    email = serializers.CharField(source = "user.email", read_only = True)
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CustomerLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ("username", "password")


class CustomerProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = "user.username", read_only = True)
    email = serializers.CharField(source = "user.email", read_only = True)
    class Meta:
        model = User
        fields = ("id","username", "email")


class CustomerPasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)
    old_password = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User
        fields = ("password", "confirm_password", "old_password")

    
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"error": "The Password confirmation does not match"}
            )
        return attrs
    
    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError({"error":"Old password is not correct"})
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance