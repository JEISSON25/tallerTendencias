from rest_framework.routers import DefaultRouter
from ..auction.views import *
from ..bid.views import *
from ..item.views import *

router = DefaultRouter()

router.register(r'auction', AuctionViewSet, basename='User')
router.register(r'bid', BidViewSet, basename='Bid')
router.register(r'item', ItemViewSet, basename='Item')

urlpatterns = router.urls