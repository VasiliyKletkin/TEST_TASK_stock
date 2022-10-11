from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    """
    API News CRUD
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


