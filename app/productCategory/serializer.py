from rest_framework import serializers
from .models import *

class productCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = product_category
        fields = ('__all__')