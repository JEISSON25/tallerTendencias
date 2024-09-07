from rest_framework import serializers
from .models import Product, User, Recommendation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'correo_electronico']