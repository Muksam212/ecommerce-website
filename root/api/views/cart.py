from ..serializers.cart import CartSerializer
from ecommerce.models import Cart

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

class CartListAPIView(ListCreateAPIView):
    serializer_class = CartSerializer
    model = Cart
    queryset = Cart.objects.all()



class CartRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    model = Cart
    queryset = Cart.objects.all()
    lookup_field = "id"


class CartListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    model = Cart
    
    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)