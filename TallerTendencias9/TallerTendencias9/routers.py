from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserViewSet, RecommendationViewSet, TopProductsViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
router.register(r'recommendations', RecommendationViewSet)
router.register(r'top-products', TopProductsViewSet, basename='top-products')

urlpatterns = [
    path('', include(router.urls)),
]
