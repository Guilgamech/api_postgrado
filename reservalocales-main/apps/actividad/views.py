from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.actividad.serializers import *

# Create your views here.

class ActividadView(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Actividad.objects.all()
