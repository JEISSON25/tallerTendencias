from django.db import models

# Create your models here.

class Event(models.Model):
    
    class Meta: 
        verbose_name = "Eventos"
        verbose_name_plural = "Eventos"
        
    name = models.CharField('Nombre', max_length=100)
    description = models.CharField('Descripción', max_length=500)
    date = models.DateField('Fecha')
    location = models.CharField('Ubicación', max_length=100)
    capacity = models.IntegerField('Capacidad')
    status_options = (
        ("ACT", "Activo"),
        ("CAN", "Cancelado"),
    )
    status = models.CharField(verbose_name='Estado', max_length=50, blank=False, null=False, choices=status_options, default='ACT')
    
    def __str__(self):
        return f"{self.name} - {self.description} - {self.date} - {self.location} - {self.capacity} - {self.status}"