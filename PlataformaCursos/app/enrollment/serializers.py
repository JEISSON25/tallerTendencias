from rest_framework import serializers 
from .models import * 

class EnrollmentSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Enrollment
        fields = ('__all__')