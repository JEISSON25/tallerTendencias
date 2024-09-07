from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer, DucumentTagSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    @action(detail=True, methods=['get'])
    def tags(self, request, pk=None):
        document = self.get_object()
        tags = document.documenttag_set.all()
        serializer = DucumentTagSerializer(tags, many=True)
        return Response(serializer.data)
