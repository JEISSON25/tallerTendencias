from restframework import serializers
from .models import Document, Tag, DocumentTag

class DucumentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTag
        fields = '_all'