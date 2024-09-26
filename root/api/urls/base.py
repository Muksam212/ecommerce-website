from .users import urlpatterns as users_urlpatterns

from django.urls import path, include

urlpatterns = [
    path('', include(users_urlpatterns))
]
