from rest_framework import serializers 
from .models import * 

class QuizSerializer(serializers.ModelSerializer): 
    nombre_course = serializers.CharField(source='id_course.nombre', read_only=True)

    class Meta: 
        model = Quiz
        fields = ['nombre_course', 'nombre']