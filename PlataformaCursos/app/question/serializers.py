from rest_framework import serializers 
from .models import * 

class QuestionSerializer(serializers.ModelSerializer): 
    Tema_quiz = serializers.CharField(source='id_quiz.nombre', read_only=True)

    class Meta: 
        model = Question
        fields = ['Tema_quiz', 'texto', 'opciones', 'respuesta_correcta']