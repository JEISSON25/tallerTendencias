from rest_framework.generics import ListAPIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderItemListView(ListAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
