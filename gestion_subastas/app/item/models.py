from django.db import models
from app.auction.models import Auction

class Item(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    subasta = models.ForeignKey(Auction, related_name='items', on_delete=models.CASCADE)
    precio_inicial = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

