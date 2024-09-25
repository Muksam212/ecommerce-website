from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    confirm_password = serializers.CharField(write_only = True, required = True)
    user_type = serializers.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password", "user_type", "user_image")

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
            bio=validated_data.get('bio', ''),
            profile_image=validated_data.get('profile_image', None),
            role=validated_data['role'],
        )
        
        # Set the password (hashing it)
        user.set_password(validated_data['password'])
        
        # Save the user to the database
        user.save()

        return user