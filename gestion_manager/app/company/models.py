from django.db import models
from ..rol.models import Rol

from django.db import models

class Product(models.Model):
    nombre_produc = models.CharField(max_length=255)
    descripcion_produc = models.TextField()
    precio_produc = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_produc

class Inventory(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.producto.nombre_produc} - {self.cantidad}"