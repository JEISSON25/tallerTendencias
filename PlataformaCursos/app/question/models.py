from django.db import models
from ..quiz.models import * 

class Question(models.Model):
    class Meta: 
        verbose_name = "Question" 
        verbose_name_plural = "Question" 
    
    texto = models.CharField("Texto", max_length=500)
    opciones = models.CharField("Opciones", max_length=500)
    respuesta_correcta = models.CharField("Respuesta Correcta", max_length=100)
    id_quiz = models.ForeignKey ( 
        Quiz, 
        verbose_name="Quiz", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True 
    )

    def __str__(self):
        return f'{self.texto}: Opciones de respuesta {self.opciones}'