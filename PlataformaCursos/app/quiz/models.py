from django.db import models
from ..course.models import * 

# Create your models here.
class Quiz(models.Model):
    class Meta: 
        verbose_name = "Quiz" 
        verbose_name_plural = "Quiz" 
    
    nombre = models.CharField("Tema", max_length=100)
    id_course = models.ForeignKey ( 
        Course, 
        verbose_name="Course", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True 
    )

    def __str__(self):
        return f'{self.nombre}'