from django.db import models
from ..store.models import *

# Create your models here.
class Products(models.Model):
    productId = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombres', max_length=100)
    descripcion = models.CharField('Descripción', max_length=250)
    precio = models.IntegerField('Precio')
    stock = models.IntegerField('Stock')
    tienda=models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.precio} {self.stock}'
   

  
