from django.shortcuts import render
from .models import Auction
from .serializer import AuctionSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class AuctionViewSet(viewsets.ModelViewSet):
    serializer_class = AuctionSerializer
    queryset = Auction.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')