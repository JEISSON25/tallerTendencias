from rest_framework import serializers
from .models import Product, Inventory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'nombre_produc', 'descripcion_produc', 'precio_produc']

class InventorySerializer(serializers.ModelSerializer):
    producto = ProductSerializer()

    class Meta:
        model = Inventory
        fields = ['id', 'producto', 'cantidad']