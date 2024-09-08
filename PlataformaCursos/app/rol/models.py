from django.db import models

# Create your models here.
class Rol(models.Model):
    class Meta: 
        verbose_name = "Rol" 
        verbose_name_plural = "Rol" 
    
    rol = models.CharField("Rol", max_length=100)

    def __str__(self):
        return f'{self.rol}'