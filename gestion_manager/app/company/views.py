from rest_framework.generics import ListAPIView, DestroyAPIView
from .models import Product, Inventory
from .serializers import ProductSerializer, InventorySerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InventoryListView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDeleteView(DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
