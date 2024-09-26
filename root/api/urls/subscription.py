from ..views.subscription import (
    SubscriptionCreateAPIView,
    SubscriptionListAPIView,
    SubscriptionAPIView
)
from django.urls import path

urlpatterns = [
    path('api/subscription/create/', SubscriptionCreateAPIView.as_view(), name = 'api-subscription-create'),
    path('api/subscription/list/', SubscriptionListAPIView.as_view(), name = 'api-subscription-list'),
    path('api/subscription/email/', SubscriptionAPIView.as_view(), name = 'api-subscription-email')
]
