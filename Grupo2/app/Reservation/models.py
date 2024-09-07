from django.db import models
from ..Event.models import *
from ..Attendee.models import *


class Reservation(models.Model):
    
    class Meta: 
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
    
    idEvent = models.ForeignKey(Event, on_delete=models.CASCADE, blank=False)
    idAttendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, blank=False)
    num_entrys = models.IntegerField(verbose_name='Numero Entradas', blank=False, null=False)
    canceled_bool = models.BooleanField(verbose_name="Cancel Reservation", default=False)
    
    def __str__(self):
        return f'{self.idEvent} - {self.idAttendee} - {self.num_entrys}'
   
