from rest_framework import serializers
from .models import Product, User, Recommendation # type: ignore

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'nombre', 'descripcion', 'precio']