from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.UserProfile.views import UserViewSet
from app.Post.views import PostViewSet
from app.Comment.views import CommentViewSet
from app.Like.views import LikeViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]


