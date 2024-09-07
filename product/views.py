from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, User, Recommendation
from .serializers import ProductSerializer, UserSerializer, RecommendationSerializer # type: ignore
from django.db.models import Avg

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class TopProductsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Recommendation.objects.values('producto_id').annotate(avg_score=Avg('puntuacion')).order_by('-avg_score')
        return Response(queryset)