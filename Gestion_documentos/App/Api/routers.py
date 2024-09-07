from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..Document.views import DocumentViewSet
from ..Tag.views import TagViewSet 
from ..DucumentTag.views import DucumentTagViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'ducument-tags', DucumentTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
