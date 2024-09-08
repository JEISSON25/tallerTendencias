from django.db import models


# Create your models here.

class Attendee(models.Model):
    
    class Meta:
        verbose_name = "Attendee"
        verbose_name_plural = "Attendee"
        
        
    nombre = models.CharField('Nombre', max_length=100)
    email = models.CharField('Email', max_length=100)

    
    
    def __str__(self):
        return f'{self.nombre} - {self.email}'