from rest_framework import viewsets
from .models import DucumentTag
from .serializers import DucumentTagSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class DucumentTagViewSet(viewsets.ModelViewSet):
    queryset = DucumentTag.objects.all()
    serializer_class = DucumentTagSerializer
