from ..serializers.users import (
    CustomerRegistration, 
    CustomerListSerializer,
    CustomerLoginSerializer, 
    CustomerProfileSerializer,
    CustomerPasswordResetSerializer
)
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from ecommerce.models import Customer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from ..views.renderers import UserRenderers

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


class CustomerRegisterAPIView(CreateAPIView):
    serializer_class = CustomerRegistration
    
    def post(self, request, format = None):
        serializer =CustomerRegistration(data = request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            user_data = self.serializer_class(user).data
            return Response(
                {"user": user_data, "msg": "Registration Success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerListSerializer

    def get(self, request, format = None):
        customer = Customer.objects.all()
        serializer = CustomerListSerializer(customer, many = True)
        return Response(serializer.data)
    

class CustomerLoginAPIView(CreateAPIView):
    serializer_class = CustomerLoginSerializer
    renderer_classes = [UserRenderers]

    def post(self, request, format = None):
        serializer = CustomerLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "username or password is not valid"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        user = request.user
        users = Customer.objects.all().filter(user = user)
        serializer = CustomerProfileSerializer(users, many = True)
        return Response(serializer.data)
    

class CustomerPasswordResetView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerPasswordResetSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset = None):
        return self.request.user

    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)

        return Response({
            'message': 'Password has been reset successfully.'
        }, status=status.HTTP_200_OK)
