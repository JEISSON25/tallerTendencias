from rest_framework.routers import DefaultRouter
from ..Event.views import *
from ..Attendee.views import *
from ..Reservation.views import *


router = DefaultRouter()

router.register(r'Event', EventViewSet, basename='Event')
router.register(r'Attendee', AttendeeViewSet, basename='Attendee')
router.register(r'Reservation', ReservationViewset, basename='Reservation')


urlpatterns = router.urls