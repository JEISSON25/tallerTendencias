from django.shortcuts import render
from .models import Bid
from .serializers import BidSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer
    queryset = Bid.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
