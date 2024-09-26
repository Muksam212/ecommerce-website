from .users import urlpatterns as users_urlpatterns
from .category import urlpatterns as category_urlpatterns
from .product import urlpatterns as product_urlpatterns
from .cart import urlpatterns as cart_urlpatterns
from .subscription import urlpatterns as subscription_urlpatterns

from django.urls import path, include

urlpatterns = [
    path('', include(users_urlpatterns)),
    path('', include(category_urlpatterns)),
    path('', include(product_urlpatterns)),
    path('', include(cart_urlpatterns)),
    path('', include(subscription_urlpatterns))
]
