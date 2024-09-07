from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..Document.views import DocumentViewSet
from ..Tag.views import TagViewSet 
from ..DucumentTag.views import DucumentTagViewSet

router = DefaultRouter()

router.register(r'documents', DocumentViewSet, basename='Documents')
router.register(r'tags', TagViewSet, basename='Tags')
router.register(r'document-tags', DucumentTagViewSet, basename='DocumentsTags')

urlpatterns = router.urls
