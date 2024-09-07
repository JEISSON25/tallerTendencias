from django.db import models

# Create your models here.

class Event(models.Model):
    
    class Meta: 
        verbose_name = "Eventos"
        verbose_name_plural = "Eventos"
        
    name = models.CharField('Nombre', max_length=100)
    description = models.CharField('Descripción', max_length=500)
    date = models.DateField('Fecha')
    