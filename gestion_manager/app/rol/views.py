from rest_framework.generics import ListAPIView
from .models import Rol
from .serializers import RolSerializer

class RolView(ListAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
