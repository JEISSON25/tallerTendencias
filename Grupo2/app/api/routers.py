from rest_framework.routers import DefaultRouter
from ..Event.views import *


router = DefaultRouter()

router.register(r'Event', EventViewSet, basename='Event')


urlpatterns = router.urls