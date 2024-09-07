from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Document
from .serializers import DocumentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    