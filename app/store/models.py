from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.direccion} - {self.telefono}"