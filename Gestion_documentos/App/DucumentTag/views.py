from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import DucumentTag
from .serializers import DucumentTagSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DucumentTagViewSet(viewsets.ModelViewSet):
    queryset = DucumentTag.objects.all()
    serializer_class = DucumentTagSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')