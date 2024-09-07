from rest_framework import viewsets
from .models import  Tag
from .serializers import TagSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

