from restframework import serializers
from .models import Document, Tag, DocumentTag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'all'

