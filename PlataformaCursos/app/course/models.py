from django.db import models
from ..user.models import * 

# Create your models here.
class Course(models.Model):
    class Meta: 
        verbose_name = "Course" 
        verbose_name_plural = "Course" 
    
    nombre = models.CharField("Nombre", max_length=100)
    descripción = models.CharField("Descripción", max_length=100)
    fecha_inicio = models.DateTimeField("Fecha de inicio")
    fecha_finalización = models.DateTimeField("Fecha de finalización")
    id_instructor = models.ForeignKey ( 
        User, 
        verbose_name="User", 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True 
    )

    def __str__(self):
        return f'{self.nombre}: {self.fecha_inicio} - {self.fecha_finalización}'