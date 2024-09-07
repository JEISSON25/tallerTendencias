from rest_framework import serializers
from .models import Order, OrderItem
from app.company.serializers import ProductSerializer
from app.rol.serializers import RolSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class OrderSerializer(serializers.ModelSerializer):
    cliente = UserSerializer()
    rol = RolSerializer()

    class Meta:
        model = Order
        fields = ['id', 'cliente', 'rol', 'fecha', 'status']

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    producto = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'producto', 'cantidad', 'precio']
