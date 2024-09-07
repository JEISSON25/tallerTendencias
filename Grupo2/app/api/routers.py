from rest_framework.routers import DefaultRouter
from ..Event.views import *
from ..Attendee.views import *


router = DefaultRouter()

router.register(r'Event', EventViewSet, basename='Event')
router.register(r'Attendee', AttendeeViewSet, basename='Attendee')


urlpatterns = router.urls