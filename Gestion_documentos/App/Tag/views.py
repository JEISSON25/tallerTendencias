from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Tag
from .serializers import TagSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')