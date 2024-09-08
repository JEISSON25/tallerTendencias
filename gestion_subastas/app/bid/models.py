from django.db import models
from django.contrib.auth.models import User
from app.auction.models import Auction

class Bid(models.Model):
    subasta = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    

    def __str__(self):
        return f"Bid by {self.usuario.username} for {self.subasta.nombre} - ${self.cantidad}"
