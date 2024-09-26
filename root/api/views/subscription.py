from ..serializers.subscription import (
    SubscriptionSerializer
)

from ecommerce.models import Subscription
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q

class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    model = Subscription

class SubscriptionListAPIView(ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    model = Subscription

class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        email = self.request.GET.get("email")

        if not email:
            return Response({"error":"Email Parameter is missing"}, status = status.HTTP_201_CREATED)
        
        # Query the Subscription model based on the email
        subscription = Subscription.objects.filter(email = email)
        if subscription.exists():
            subscription = subscription.first()

            if subscription.status:
                data = {
                    "message": "Subscription is active.",
                    "name": subscription.name,
                    "email": subscription.email,
                    "status": subscription.status
                }
                return Response({"data":data}, status=status.HTTP_200_OK)
            else:
                data = {
                    "message": "Subscription is not active.",
                    "name": subscription.name,
                    "email": subscription.email,
                    "status": subscription.status
                }
                return Response({"data":data}, status=status.HTTP_200_OK)
        else:
            # Handle case where the subscription is not found
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)