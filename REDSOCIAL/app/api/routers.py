from rest_framework.routers import DefaultRouter
from ..Comment.views import *
from ..Post.views import *
from ..UserProfile.views import *
from ..Like.views import *
# Crea una instancia del router
router = DefaultRouter()

# Registra los viewsets
router.register(r'profiles', UserProfileViewSet, basename='profiles')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'likes', LikeViewSet, basename='likes')

# Exporta las rutas para ser usadas en urls.py
urlpatterns = router.urls
