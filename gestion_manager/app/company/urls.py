from django.urls import path
from .views import ProductListView, InventoryListView, InventoryDeleteView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDeleteView.as_view(), name='inventory-delete'),
]