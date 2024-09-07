from django.urls import path
from .views import OrderListView, OrderItemListView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order-items/', OrderItemListView.as_view(), name='order-item-list'),
]
