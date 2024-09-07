from rest_framework import serializers 
from .models import * 

class EnrollmentSerializer(serializers.ModelSerializer): 
    nombre_course = serializers.CharField(source='idCourse.nombre', read_only=True)
    nombre_estudiante = serializers.CharField(source='idUser.nombre', read_only=True)
    apellido_estudiante = serializers.CharField(source='idUser.apellido', read_only=True)

    class Meta: 
        model = Enrollment
        fields = ['nombre_course', 'nombre_estudiante', 'apellido_estudiante', 'fecha']