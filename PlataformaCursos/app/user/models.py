from django.db import models

# Create your models here.
class User(models.Model):
    class Meta: 
        verbose_name = "User" 
        verbose_name_plural = "Users" 
    
    nombre = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_length=100)
    documento = models.CharField("Documento", max_length=100)
    telefono = models.CharField("Teléfono", max_length=100)
    Email = models.EmailField("Email", max_length=100)
    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'