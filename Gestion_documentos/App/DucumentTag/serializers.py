from rest_framework import serializers
from .models import DucumentTag

class DucumentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DucumentTag
        fields = '__all__'