from django.urls import path
from .views import RolView

urlpatterns = [
    path('roles/', RolView.as_view(), name='roles-list'),
]