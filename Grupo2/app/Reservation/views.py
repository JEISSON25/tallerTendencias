from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('idEvent__name', 'idAttendee__nombre', 'num_entrys')
    ordering_fields = ('__all__')